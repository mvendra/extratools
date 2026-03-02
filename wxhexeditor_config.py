#!/usr/bin/env python3

import sys
import os

def create_wxhexeditor_config():

    target_path = "~/.wxHexEditor"
    target_path = os.path.expanduser(target_path)

    if os.path.exists(target_path):
        print("Target path [%s] already exists! Aborting." % target_path)
        return False

    output = ""
    output += "Language=English (United States)"
    output += "ScreenX=100\n"
    output += "ScreenY=100\n"
    output += "ScreenW=600\n"
    output += "ScreenH=400\n"
    output += "ScreenFullScreen=0\n"

    with open(target_path, "w") as f:
        f.write(output)

    return True

if __name__ == "__main__":

    if not create_wxhexeditor_config():
        print("Operation failed")
        sys.exit(1)
