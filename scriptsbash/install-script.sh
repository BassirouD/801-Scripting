#!/bin/bash

archive_name=$1
base_folder=$2

if [ $# == 2 ]; then
    echo "Parameters ok..."

else
    echo "Parameters not ok..."
    exit 1
fi

if [ -e $archive_name ]; then
    echo "File exist"
    echo "Decompression file"
fi