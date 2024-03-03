#!/usr/bin/env python3

import sys
import os

def unit_multip(str_input):

    str_input_lc = str_input.lower()

    if str_input_lc == "kb":
        return 1024
    elif str_input_lc == "mb":
        return 1024*1024
    elif str_input_lc == "gb":
        return 1024*1024*1024
    elif str_input_lc == "tb":
        return 1024*1024*1024*1024

    return None

def to_bytes(str_input):

    last_space = str_input.rfind(" ")
    numbers_only = str_input[:last_space]
    the_unit = str_input[last_space+1:]
    return int(numbers_only) * unit_multip(the_unit)

def mem_swap_check():

    contents = None
    with open("/proc/meminfo") as f:
        contents = f.read()

    total_swap = None
    free_swap = None
    used_swap = None

    for l in contents.split("\n"):
        if "SwapTotal:" in l:
            total_swap = (l[10:].strip())
        elif "SwapFree:" in l:
            free_swap = (l[9:].strip())

    total_swap = to_bytes(total_swap)
    free_swap = to_bytes(free_swap)
    used_swap = (total_swap - free_swap)

    if used_swap == 0:
        print("No swap being currently used")
    else:
        percent_used = (100.0/total_swap) * used_swap
        print("%d%% of swap being used" % percent_used)

    return True

if __name__ == "__main__":

    if not mem_swap_check():
        print("Operation failed")
        sys.exit(2)
