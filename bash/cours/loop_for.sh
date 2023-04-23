#!/bin/bash

if [ $# -le 3 ]; then
    echo "Au moins 4 arguments"
    exit 1
fi

echo "Les paramétres sont: "
for variable in $*; do
    echo "$variable"
done

if [ $# -ne 1 ]; then
    echo usage "$0" repertoire
    exit 1
fi

#*******************************************************

for f in $(ls $1); do
    if [ -f "$1/$f" ]; then
        echo "$f" est fichier
    elif [ -d "$1/$f" ]; then
        echo "$f" est un respertoire
    fi
done
exit 0
#*******************************************************