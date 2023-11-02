#!/usr/bin/env python3

import sys
import os
import subprocess

def quicksquash(target_repo, num_commits):

    git_bin_win = "/usr/bin/git.exe"
    git_bin_lin = "/usr/bin/git"
    git_bin = git_bin_win
    if not os.path.exists(git_bin):
        git_bin = git_bin_lin

    head_plus_num = "HEAD~%s" % num_commits
    cmd_list = [git_bin, "-C", target_repo, "reset", "--soft", head_plus_num]

    try:
        process = subprocess.run(cmd_list, input=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=os.getcwd(), check=False, encoding="utf8", errors=None, env=os.environ, timeout=120)
        if process.returncode != 0:
            print(process.stdout)
            print(process.stderr)
            return False
    except Exception as ex:
        print( str(ex) )
        return False

    print("Repository [%s] has been compressed by [%s] commits" % (target_repo, num_commits))
    return True

def puaq():
    print("Usage: %s target_repo src_folder" % os.path.basename(__file__))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 3:
        puaq()

    target_repo = sys.argv[1]
    target_repo = os.path.abspath(target_repo)
    num_commits = sys.argv[2]

    if not quicksquash(target_repo, num_commits):
        print("Operation failed")
        sys.exit(2)
