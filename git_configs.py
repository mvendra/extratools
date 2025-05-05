#!/usr/bin/env python3

import sys
import os
import subprocess

def _run_git_command(cmd):

    git_bin_win = "/usr/bin/git.exe"
    git_bin_lin = "/usr/bin/git"
    git_bin = git_bin_win
    if not os.path.exists(git_bin):
        git_bin = git_bin_lin

    cmd_full = [git_bin]
    for c in cmd:
        cmd_full.append(c)

    try:
        process = subprocess.run(cmd_full, input=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=os.getcwd(), check=False, encoding="utf8", errors=None, env=os.environ, timeout=120)
        if process.returncode != 0:
            print(process.stdout)
            print(process.stderr)
            return False, "cmd [%s] failed" % cmd
    except Exception as ex:
        print( str(ex) )
        return False

    return True, None

def _config(key, value=None, global_cfg=True):

    cmd = ["config"]
    if global_cfg:
        cmd.append("--global")
    cmd.append(key)
    if value is not None:
        cmd.append(value)

    return _run_git_command(cmd)

def _call_and_assemble_report(report, cfg_key, cfg_val):

    v, r = _config(cfg_key, cfg_val, True)
    if not v:
        report.append(r)
    return report

def set_git_configs(name, email):

    report = _call_and_assemble_report([], "user.name", name)
    report = _call_and_assemble_report(report, "user.email", email)

    if len(report) > 0:
        print("Failures:")
        for ri in report:
            print(ri)
        sys.exit(1)
    else:
        print("All OK")

if __name__ == "__main__":

    name = input("Input your name.\n")
    email = input("Input your email.\n")
    set_git_configs(name, email)
