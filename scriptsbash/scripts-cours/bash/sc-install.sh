#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Paramètres manquant...."
    exit 1
fi

archive_name=$1
install_folder=$2

if [ -e $archive_name ]; then
    echo "Décompression"
    extension=${archive_name##*.}
    if [ $extension == "tar" -o $extension == "tgz" ]; then
        tar xvf $archive_name -C $install_folder
    else
        if [ $extension == "zip" ]; then
            unzip -q $archive_name -d $install_folder
        fi
    fi

else
    echo "Le fichier n'existe pas"
fi

exit 0