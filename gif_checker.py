#!/usr/bin/env python3

import sys
import os

def gif_checker(input_path):

    contents = None
    with open(input_path, mode="rb") as f:
        contents = f.read()

    if len(contents) < 6:
        return False

    if not (contents[0] == 0x47 and contents[1] == 0x49 and contents[2] == 0x46 and contents[3] == 0x38 and contents[4] == 0x39 and contents[5] == 0x61):
        return False

    return True

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Missing input param")
        sys.exit(2)

    if not gif_checker(sys.argv[1]):
        print("GIF not detected")
        sys.exit(1)
    print("GIF detected")
