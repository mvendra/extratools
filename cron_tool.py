#!/usr/bin/env python3

import sys
import os
import subprocess

import path_utils

def run_cron(params):

    cmd_list = ["crontab"]
    for p in params:
        cmd_list.append(p)

    contents = ""
    try:
        process = subprocess.run(cmd_list, input=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=os.getcwd(), check=False, encoding="utf8", errors=None, env=os.environ, timeout=120)
        if process.returncode != 0:
            print(process.stdout)
            print(process.stderr)
            return False
        contents = process.stdout
    except Exception as ex:
        print( str(ex) )
        return False

    return contents

def cron_tool_export(filename):

    contents = run_cron(["-l"])
    with open(filename, "w") as f:
        f.write(contents)

def cron_tool_import(filename):

    run_cron([filename])

def puaq():
    print("Usage: %s operation filename" % path_utils.basename_filtered(__file__))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 3:
        puaq()

    operation = sys.argv[1]
    filename = sys.argv[2]

    if operation == "export":
        cron_tool_export(filename)
    elif operation == "import":
        cron_tool_import(filename)
    else:
        sys.exit(1)
        print("Unknown operation")
