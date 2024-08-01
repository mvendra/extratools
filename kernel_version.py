#!/usr/bin/env python3

import sys
import os

def not_number_or_dash_or_dot(input):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "."]
    if input in numbers:
        return False
    return True

def kernel_version():

    contents = None
    with open("/proc/sys/kernel/osrelease") as f:
        contents = f.read()
    contents = contents.strip()

    final_str = None
    for i in range(len(contents)):
        if not_number_or_dash_or_dot(contents[i]):
            final_str = contents[0:i-1]
            break

    print(final_str)
    return True

if __name__ == "__main__":

    if not kernel_version():
        print("Operation failed")
        sys.exit(2)
