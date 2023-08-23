#!/usr/bin/env python3

import sys
import os
import shutil
import subprocess

def get_repo_name(target):

    result = ""
    pos = target.rfind("/")
    result = target[pos+1:]
    return result

def retry_repo_delegate(target):

    git_bin = "/usr/bin/git.exe"
    cmd_list = [git_bin, "clone", target]

    try:
        process = subprocess.run(cmd_list, input=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=os.getcwd(), check=False, encoding="utf8", errors=None, env=os.environ, timeout=120)
        if process.returncode != 0:
            print(process.stdout)
            print(process.stderr)
            return False
    except Exception as ex:
        print( str(ex) )
        return False

    return True

def retry_repo(target):

    local_base = os.getcwd()
    local_repo = get_repo_name(target)
    full_final_target = os.path.join(local_base, local_repo)

    if os.path.exists(full_final_target):
        print("[%s] already exists. Aborting..." % full_final_target)
        return False

    max_retries = 8
    count = 0
    while (count < max_retries):
        count += 1

        if retry_repo_delegate(target):
            print("Attempt [%d] succeeded\n" % count)
            return True
        else:
            print("Attempt [%d] failed - will retry\n" % count)
            shutil.rmtree(full_final_target)

    return False

def puaq():
    print("Usage: %s URL" % path_utils.basename_filtered(__file__))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        puaq()

    target = sys.argv[1]
    if not retry_repo(target):
        print("All attempts failed")
        sys.exit(1)
