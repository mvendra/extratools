#!/usr/bin/env python3

import sys
import os

def list_int_files(target):

    objfiles = []

    for path, dirnames, filenames in os.walk(target):
        for entry in filenames:
            filename, file_extension = os.path.splitext(entry)
            if file_extension == ".o":
                objfiles.append(os.path.join(path, entry))

    return True, objfiles

def puaq():
    print("Usage: %s path" % os.path.basename(__file__))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        puaq()

    target = sys.argv[1]
    v, r = list_int_files(target)
    if not v:
        print("Failed!")

    for i in r:
        print(i)
