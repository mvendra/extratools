#!/bin/bash

SHA_APP=""

if [[ "$unamestr" == 'Linux' ]]; then
    SHA_APP="sha256sum"
else
    SHA_APP="shasum -a 256"
fi

RFN=(`date +%s | $SHA_APP | base64 | head -c 48`)
RFN=${RFN}.tmp

if [ -e $RFN ]; then
  echo "Temporary file $RFN already exists! Aborting."
  exit 1
fi

echo -n $RFN

