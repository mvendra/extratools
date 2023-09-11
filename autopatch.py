#!/usr/bin/env python3

import sys
import os
import subprocess

def filter_files(base_folder, patch_candidates):

    base_folder_resolved = os.path.realpath(base_folder)
    patch_candidates_filtered = []

    for x in patch_candidates:
        if x.endswith(".patch"):
            patch_candidates_filtered.append(os.path.join(base_folder_resolved, x))

    return patch_candidates_filtered

def try_apply(repo, file):

    git_bin_win = "/usr/bin/git.exe"
    git_bin_lin = "/usr/bin/git"
    git_bin = git_bin_win
    if not os.path.exists(git_bin):
        git_bin = git_bin_lin

    cmd_list = [git_bin, "-C", repo, "apply", file]

    try:
        process = subprocess.run(cmd_list, input=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=os.getcwd(), check=False, encoding="utf8", errors=None, env=os.environ, timeout=120)
        if process.returncode != 0:
            print(process.stdout)
            print(process.stderr)
            return False
    except Exception as ex:
        print( str(ex) )
        return False

    print("Patch [%s] applied" % file)
    return True

def run_round(patches, target_repo):

    target_repo_resolved = os.path.realpath(target_repo)
    not_applied_yet = []
    for x in patches:

        if not try_apply(target_repo_resolved, x):
            not_applied_yet.append(x)

    return not_applied_yet

def autopatch(src_folder, target_repo):

    patch_candidates = os.listdir(src_folder)
    patch_candidates_filtered = filter_files(src_folder, patch_candidates)

    MAX_ITERATIONS = len(patch_candidates_filtered) * 5
    c = 0

    while len(patch_candidates_filtered) > 0:

        c += 1
        if c == MAX_ITERATIONS:
            return False

        patch_candidates_filtered = run_round(patch_candidates_filtered, target_repo)

    return True

def puaq():
    print("Usage: %s src_folder target_repo" % os.path.basename(__file__))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) < 3:
        puaq()

    src_folder = sys.argv[1]
    target_repo = sys.argv[2]

    if not autopatch(src_folder, target_repo):
        print("Operation failed")
        sys.exit(2)
