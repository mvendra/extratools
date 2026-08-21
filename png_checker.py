#!/usr/bin/env python3

import sys
import os

def png_checker(input_path):

    contents = None
    with open(input_path, mode="rb") as f:
        contents = f.read()

    if len(contents) < 4:
        return False

    if contents[1] == 0x50 and contents[2] == 0x4e and contents[3] == 0x47:
        return True

    return False

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Missing input param")
        sys.exit(2)

    if not png_checker(sys.argv[1]):
        print("PNG not detected")
        sys.exit(1)
    print("PNG detected")
