#!/usr/bin/env python3

import sys
import os

def create_codelite_config():

    target_path = "~/.codelite-gdbinit"
    target_path = os.path.expanduser(target_path)

    if os.path.exists(target_path):
        print("Target path [%s] already exists! Aborting." % target_path)
        return False

    output = ""
    output += "set disassembly-flavor intel\n"
    output += "python\n"
    output += "import sys\n"
    output += "sys.path.insert(0, '$CodeLiteGdbPrinters')\n"
    output += "\n"
    output += "from libstdcxx.v6.printers import register_libstdcxx_printers\n"
    output += "register_libstdcxx_printers (None)\n"
    output += "\n"
    output += "from qt4 import register_qt4_printers\n"
    output += "register_qt4_printers (None)\n"
    output += "\n"
    output += "from wx import register_wx_printers\n"
    output += "register_wx_printers (None)\n"
    output += "\n"
    output += "end"

    with open(target_path, "w") as f:
        f.write(output)

    return True

if __name__ == "__main__":

    if not create_codelite_config():
        print("Operation failed")
        sys.exit(1)
