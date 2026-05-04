#!/usr/bin/env python3

import sys
import os

def mkdir_ign(target_path):

    try:
        os.mkdir(target_path)
    except FileExistsError as fieex:
        pass

def gen_config_contents():

    output = ""

    output += "{\n"
    output += "    \"hex.builtin.setting.data_inspector\": {\n"
    output += "        \"hex.builtin.setting.data_inspector.hidden_rows\": null\n"
    output += "    },\n"
    output += "}\n"

    return output

def create_imhex_config():

    target_base1 = "~/.config/"
    target_base2 = "~/.config/imhex/"
    target_base3 = "~/.config/imhex/config/"
    target_path = "~/.config/imhex/config/settings.json"

    target_base1 = os.path.abspath(os.path.expanduser(target_base1))
    target_base2 = os.path.abspath(os.path.expanduser(target_base2))
    target_base3 = os.path.abspath(os.path.expanduser(target_base3))
    target_path = os.path.abspath(os.path.expanduser(target_path))

    if os.path.exists(target_path):

        print("Target [%s] already exists. Aborting." % target_path)
        return False

    else:

        mkdir_ign(target_base1)
        mkdir_ign(target_base2)
        mkdir_ign(target_base3)

        output = gen_config_contents()

        with open(target_path, "w") as f:
            f.write(output)

    return True

if __name__ == "__main__":

    if not create_imhex_config():
        print("Operation failed")
        sys.exit(1)
