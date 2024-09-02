#!/usr/bin/env python3

import sys
import os
import shutil
import subprocess

def retry_repo_delegate(target):

    cmd_list = [target]

    try:
        process = subprocess.run(cmd_list, input=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=os.getcwd(), check=False, encoding="utf8", errors=None, env=os.environ, timeout=120)
        if process.returncode != 0:
            fail_detail = "[%s] - [%s]" % (process.stdout, process.stderr)
            return False, fail_detail
    except Exception as ex:
        print(str(ex))
        sys.exit(1)

    return True, None

def applet_stress_test(target, number_runs):

    ok_count = 0
    nok_count = 0
    failures_details = []

    count = 0
    while (count < int(number_runs)):
        count += 1

        v, r = retry_repo_delegate(target)
        if v:
            ok_count += 1
        else:
            nok_count += 1
            failures_details.append(r)

    return (ok_count, nok_count, failures_details)

def puaq():
    print("Usage: %s path-to-cmd number-runs" % os.path.basename(__file__))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        puaq()

    target = sys.argv[1]
    nr_runs = sys.argv[2]

    ok_count, nok_count, failures_details = applet_stress_test(target, nr_runs)

    print("[%d] passes, [%d] fails:" % (ok_count, nok_count))
    idx = 0
    for entry in failures_details:
        idx += 1
        print("[%d]: %s" % (idx, entry))
