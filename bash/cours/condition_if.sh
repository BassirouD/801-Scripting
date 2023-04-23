#!/bin/bash

if [ $# -ne 1 ]; then
    echo usage: "$0" argument
    exit 1
fi
echo Le parametre est: "$1"
exit 0
