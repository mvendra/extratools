#!/bin/sh

PYBOOTFILE="main.py"
if [ ! -z "$1" ]; then
    PYBOOTFILE="$1"
fi

if [ -e ./"$PYBOOTFILE" ]; then
    echo "There's already a ./$PYBOOTFILE in the CWD (`pwd -P`), so this script is aborted."
    exit 1
fi

touch ./"$PYBOOTFILE"
echo "#!/usr/bin/env python\n\nimport sys\nimport os\n\nif __name__ == \"__main__\":\n\n    print(\"hello world\")" > ./"$PYBOOTFILE"