#!/usr/bin/env python3
"""Check Linux random-seed health and kernel entropy availability.

This script cannot prove the true entropy of an arbitrary seed file. Instead,
it performs a practical verification:

* reads the kernel entropy pool from /proc/sys/kernel/random/entropy_avail
* checks that a seed file exists and is non-empty
* reports the seed file size and mode for a quick sanity check

Exit status:
  0 when the configured entropy threshold is met and the seed file looks valid
  1 when the system does not meet the requested checks
"""

from __future__ import annotations

import argparse
import os
import stat
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_SEED_PATHS = (
    Path("/var/lib/systemd/random-seed"),
    Path("/var/lib/random-seed"),
)


@dataclass(frozen=True)
class SeedReport:
    path: Path | None
    exists: bool
    size_bytes: int | None
    mode: str | None


def read_int_file(path: Path) -> int | None:
    try:
        return int(path.read_text(encoding="utf-8").strip())
    except (OSError, ValueError):
        return None


def select_seed_path(explicit_path: Path | None) -> Path | None:
    if explicit_path is not None:
        return explicit_path

    for candidate in DEFAULT_SEED_PATHS:
        if candidate.exists():
            return candidate

    return DEFAULT_SEED_PATHS[0]


def inspect_seed_file(path: Path | None) -> SeedReport:
    if path is None:
        return SeedReport(path=None, exists=False, size_bytes=None, mode=None)

    try:
        stat_result = path.stat()
    except OSError:
        return SeedReport(path=path, exists=False, size_bytes=None, mode=None)

    mode = stat.filemode(stat_result.st_mode)
    return SeedReport(
        path=path,
        exists=True,
        size_bytes=stat_result.st_size,
        mode=mode,
    )


def format_seed_report(report: SeedReport) -> str:
    if report.path is None:
        return "seed file: not configured"

    if not report.exists:
        return f"seed file: missing ({report.path})"

    return (
        f"seed file: {report.path} | size={report.size_bytes} bytes | mode={report.mode}"
    )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Verify Linux random-seed health and entropy availability."
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=256,
        help="Minimum entropy_avail required for success (default: 256).",
    )
    parser.add_argument(
        "--seed-file",
        type=Path,
        default=None,
        help="Explicit random-seed file to inspect.",
    )
    args = parser.parse_args(argv)

    entropy_avail = read_int_file(Path("/proc/sys/kernel/random/entropy_avail"))
    pool_size = read_int_file(Path("/proc/sys/kernel/random/poolsize"))
    seed_path = select_seed_path(args.seed_file)
    seed_report = inspect_seed_file(seed_path)

    print("Linux random-seed verification")
    print("--------------------------------")

    if entropy_avail is None:
        print("entropy_avail: unavailable")
    else:
        pool_info = f" / poolsize={pool_size}" if pool_size is not None else ""
        print(f"entropy_avail: {entropy_avail}{pool_info}")

    print(format_seed_report(seed_report))

    problems: list[str] = []

    if entropy_avail is None:
        problems.append("could not read the kernel entropy pool")
    elif entropy_avail < args.threshold:
        problems.append(
            f"entropy_avail {entropy_avail} is below threshold {args.threshold}"
        )

    if not seed_report.exists:
        problems.append("seed file is missing or unreadable")
    elif seed_report.size_bytes == 0:
        problems.append("seed file is empty")

    if problems:
        print("status: FAIL")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("status: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))