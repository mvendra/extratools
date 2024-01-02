#!/usr/bin/env python3

import sys
import os

DB_FILENAME = "pwd_bookmarker.db"

def make_db_fn(db_folder):

    final_fn = os.path.join(db_folder, DB_FILENAME)
    return final_fn

def read_file(fn_target):

    contents = ""
    if not os.path.exists(fn_target):
        return ""
    with open(fn_target, "r") as f:
        contents = f.read()
    return contents

def write_file(fn_target, contents):

    with open(fn_target, "w") as f:
        f.write(contents)

def pwd_bookmarker_push(db_folder):

    file_contents = read_file(make_db_fn(db_folder))
    pwd = os.getcwd()
    if file_contents == "":
        file_contents += "%s" % pwd
    else:
        file_contents += "\n%s" % pwd
    write_file(make_db_fn(db_folder), file_contents)

    return True

def pwd_bookmarker_pop(db_folder):

    file_contents = read_file(make_db_fn(db_folder))
    file_contents_list = file_contents.split("\n")
    file_contents_list.pop()
    file_contents = ""

    idx = 0
    for fc in file_contents_list:
        idx += 1

        if idx == 1:
            file_contents += "%s" % fc
        else:
            file_contents += "\n%s" % fc

    write_file(make_db_fn(db_folder), file_contents)
    return True

def pwd_bookmarker_top(db_folder):

    file_contents = read_file(make_db_fn(db_folder))
    file_contents_list = file_contents.split("\n")
    tos = file_contents_list[len(file_contents_list)-1]
    print(tos)

    return True

def pwd_bookmarker(db_folder, operation):

    if operation == "push":
        return pwd_bookmarker_push(db_folder)
    elif operation == "pop":
        return pwd_bookmarker_pop(db_folder)
    elif operation == "top":
        return pwd_bookmarker_top(db_folder)

    return False

def puaq():
    print("Usage: %s db_folder operation (push|pop|top)" % os.path.basename(__file__))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 3:
        puaq()

    db_folder = sys.argv[1]
    operation = sys.argv[2]

    valid_ops = ["push", "pop", "top"]
    if not operation in valid_ops:
        sys.exit(2)

    if not pwd_bookmarker(db_folder, operation):
        print("Operation failed")
        sys.exit(3)
