#!/usr/bin/env python3

import sys
import os
import stat

def check_permission(path):
    p = os.stat(path)
    if p.st_mode & stat.S_IRWXG:
        return False # has group permissions
    if p.st_mode & stat.S_IRWXO:
        return False # has permissions for others
    return True

def check_auth_folder(path):

    items = []
    for dirpath, dirnames, filenames in os.walk(path, followlinks=False):
        for fns in filenames:
            items.append(os.path.join(path, fns))

    result = True
    for f in items:
        if not check_permission(f):
            print("%s has bad permissions." % f)
            result = False

    return result

def check_auth(paths):

    for p in paths:
        if not os.path.exists(p):
            print("Path [%s] does not exist." % p)
            return

    any_errors = False
    for p in paths:
        if not check_auth_folder(p):
            any_errors = True
            print("Path [%s]: Incorrect permissions detected." % p)

    if not any_errors:
        print("All good.")
    else:
        print("Errors detected.")

def puaq():
    print("Usage: %s [path1 | path2]" % os.path.basename(__file__))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        puaq()
    paths = sys.argv[1:]

    check_auth(paths)
