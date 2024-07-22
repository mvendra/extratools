#!/bin/bash

puaq(){ # puaq stands for Print Usage And Quit
    echo "Usage: `basename $0` param"
    exit 1
}

if [ -z $1 ]; then
    puaq
fi

TARGET=$1
TARGET_BZ2=$TARGET.bz2
TARGET_BZ2_SHA512=$TARGET_BZ2.sha512

if [ ! -f $TARGET ]; then
    echo "$TARGET does not exist."
    exit 2
fi

if [ -f $TARGET_BZ2 ]; then
    echo "$TARGET_BZ2 already exists."
    exit 3
fi

if [ -f $TARGET_BZ2_SHA512 ]; then
    echo "$TARGET_BZ2_SHA512 already exists."
    exit 3
fi

bzip2 $TARGET
sha512sum $TARGET_BZ2 > $TARGET_BZ2_SHA512
