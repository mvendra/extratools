#!/usr/bin/env python3

import sys
import os

def disk_info():

    contents = None
    with open("/etc/fstab") as f:
        contents = f.read()

    for l in contents.split("\n"):

        if len(l) < 6:
            continue

        if l[0:5] == "UUID=":

            p = l.find(" ")
            if p == -1:
                continue

            mntp = (l[p:]).strip()

            p = mntp.find(" ")
            if p == -1:
                continue

            mntp = (mntp[0:p]).strip()
            print("%s" % mntp)

    return True

if __name__ == "__main__":

    if not disk_info():
        print("Operation failed")
        sys.exit(1)
