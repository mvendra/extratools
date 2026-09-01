#!/usr/bin/env python3

import sys
import os

def png_checker(input_path):

    contents = None
    with open(input_path, mode="rb") as f:
        contents = f.read()

    if len(contents) < 7:
        return False

    if contents[0] == 0x42 and contents[1] == 0x4d:
        return True

    return False

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Missing input param")
        sys.exit(2)

    if not png_checker(sys.argv[1]):
        print("BMP not detected")
        sys.exit(1)
    print("BMP detected")
