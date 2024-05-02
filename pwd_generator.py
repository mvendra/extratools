#!/usr/bin/env python3

import sys
import os

from random import randrange

def pwd_generator():

    pwdlen = 18
    srcdict = "qwertyuiopasdfghjklzxcvbnm,.QWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*-=_+"
    srcdict_list = []
    for c in srcdict:
        srcdict_list.append(c)
    gen_pwd = ""

    for i in range(pwdlen):
        random_index = randrange(len(srcdict))
        gen_pwd += srcdict_list[random_index]

    print(gen_pwd)

if __name__ == "__main__":
    pwd_generator()
