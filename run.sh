#!/usr/bin/env bash
SPOONABLE_DIR=$(dirname -- "$( readlink -f -- "$0"; )";)
cd $SPOONABLE_DIR
python3 spoonable.py