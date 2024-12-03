#!/usr/bin/env python3

import sys
import os

def set_gdb_asm_intel_flavor():

    target_path = "~/.gdbinit"
    target_path = os.path.expanduser(target_path)

    output = "set disassembly-flavor intel\n"

    if not os.path.exists(target_path):
        with open(target_path, "w") as f:
            f.write(output)

    contents = ""
    with open(target_path, "r") as f:
        contents = f.read()

    has_out = False
    for l in contents.split("\n"):
        if l.strip() == output.strip():
            has_out = True

    if not has_out:
        contents = "%s\n%s\n" % (contents, output)
        with open(target_path, "w") as f:
            f.write(contents)

    return True

if __name__ == "__main__":

    if not set_gdb_asm_intel_flavor():
        print("Operation failed")
        sys.exit(1)
