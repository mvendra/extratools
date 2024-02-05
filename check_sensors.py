#!/usr/bin/env python3

import sys
import os
import subprocess

def check_sensors():

    sensors_bin = "sensors"
    cmd_list = [sensors_bin]

    try:
        process = subprocess.run(cmd_list, input=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=os.getcwd(), check=False, encoding="utf8", errors=None, env=os.environ, timeout=120)
        if process.returncode != 0:
            print(process.stdout)
            print(process.stderr)
            return False
    except Exception as ex:
        print( str(ex) )
        return False

    data = {}

    # first step - separate sections
    new_section_next = True
    current_section = None
    for l in process.stdout.split("\n"):

        if l == "":
            new_section_next = True
            continue

        if new_section_next:
            current_section = l
            data[current_section] = []
            new_section_next = False
            continue

        data[current_section].append(l)

    warn_temp = 80
    no_warnings = True

    # second step - check temperatures
    for k in data:
        for v in data[k]:

            if len(v.strip()) > 0:
                if (v.strip())[0] == "(":
                    continue

            f2 = v.find("°C")
            if f2 == -1:
                continue

            f1 = v.rfind("+", 0, f2)

            cur_temp = float(v[f1+1:f2])
            if cur_temp >= warn_temp:
                print("WARNING: check the temperature of [%s]" % k)
                no_warnings = False

    if no_warnings:
        print("No issues found")

    return True

if __name__ == "__main__":

    if not check_sensors():
        print("Operation failed")
        sys.exit(2)
