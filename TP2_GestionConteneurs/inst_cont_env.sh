#!/bin/bash

#sudo apt update
#sudo apt install -y lxc lxd bridge-utils

sudo apt update
sudo apt install -y lxc 
sudo apt install -y lxc-templates


if [ $? -ne 0 ]; then
    echo "L'installation des packages a échoué"
else
    echo "L'installation des packages a réussi"
fi

exit 0