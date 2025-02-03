#!/usr/bin/env python3

import sys
import os

def set_tmux_color_config():

    target_path = "~/.tmux.conf"
    target_path = os.path.expanduser(target_path)

    output = "set -g default-terminal \"screen-256color\"\n"

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

    if not set_tmux_color_config():
        print("Operation failed")
        sys.exit(1)
