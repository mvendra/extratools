#!/usr/bin/env python3

import sys
import os
import subprocess

def bkbranch(target_repo):

    git_bin_win = "/usr/bin/git.exe"
    git_bin_lin = "/usr/bin/git"
    git_bin = git_bin_win
    if not os.path.exists(git_bin):
        git_bin = git_bin_lin

    cmd_list = [git_bin, "-C", target_repo, "branch"]

    try:
        process = subprocess.run(cmd_list, input=None, capture_output=True, shell=False, cwd=os.getcwd(), check=False, encoding="utf8", errors=None, env=os.environ, timeout=120)
        if process.returncode != 0:
            print(process.stdout)
            print(process.stderr)
            return False
    except Exception as ex:
        print( str(ex) )
        return False

    current_branch = process.stdout
    current_branch = current_branch[2:]
    current_branch = current_branch.strip()
    backup_branch = "%s_bk" % current_branch

    cmd_list.clear()
    cmd_list = [git_bin, "-C", target_repo, "branch", backup_branch]

    try:
        process = subprocess.run(cmd_list, input=None, capture_output=True, shell=False, cwd=os.getcwd(), check=False, encoding="utf8", errors=None, env=os.environ, timeout=120)
        if process.returncode != 0:
            print(process.stdout)
            print(process.stderr)
            return False
    except Exception as ex:
        print( str(ex) )
        return False

    print("Repository [%s] current branch [%s] has been backed up as [%s]" % (target_repo, current_branch, backup_branch))
    return True

def puaq():
    print("Usage: %s target_repo" % os.path.basename(__file__))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        puaq()

    target_repo = sys.argv[1]
    target_repo = os.path.abspath(target_repo)

    if not bkbranch(target_repo):
        print("Operation failed")
        sys.exit(2)
