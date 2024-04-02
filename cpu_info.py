#!/usr/bin/env python3

import sys
import os

def sanitize_model_name(input):
    f = input.find(":")
    return (input[f+1:]).strip()

def cpu_info():

    contents = None
    with open("/proc/cpuinfo") as f:
        contents = f.read()

    model = ""
    cores = 0

    for l in contents.split("\n"):
        if l[0:9] == "processor":
            cores += 1
        elif l[0:10] == "model name":
            model = sanitize_model_name(l)

    print("Processor model: %s" % model)
    print("Processor cores: %s" % cores)

    return True

if __name__ == "__main__":

    if not cpu_info():
        print("Operation failed")
        sys.exit(2)
