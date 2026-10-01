#!/usr/bin/env python3

import sys
import os

def jpg_checker(input_path):

    contents = None
    with open(input_path, mode="rb") as f:
        contents = f.read()

    if len(contents) < 6:
        return False

    if not (contents[0] == 0xFF and contents[1] == 0xD8):
        return False

    if not (contents[2] == 0xFF and contents[3] == 0xE0):
        return False

    header_payload_size = (contents[4] << 8) + contents[5]

    if len(contents) < header_payload_size + 6:
        return False

    for i in range(header_payload_size):

        if contents[6+i] == 0x4A: # J
            if i == header_payload_size-1:
                break
            if contents[6+i+1] == 0x46: # F
                if i == header_payload_size-2:
                    break
                if contents[6+i+2] == 0x49: # I
                    if i == header_payload_size-3:
                        break
                    if contents[6+i+3] == 0x46: # F
                        if i == header_payload_size-4:
                            break
                        if contents[6+i+4] == 0x00: # NULL
                            if i == header_payload_size-5:
                                break
                            return True

    return False

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Missing input param")
        sys.exit(2)

    if not jpg_checker(sys.argv[1]):
        print("JPG not detected")
        sys.exit(1)
    print("JPG detected")
