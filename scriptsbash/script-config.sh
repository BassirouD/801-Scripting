#!/bin/bash

#Script bash de configuration

hostname=$1
id_carte_reseau=$2
address_reseau=$3
address_passerelle=$4
address_dns=$5

if [ $# == 5 ]; then
    echo "Good....."
else
    echo "Bad..."
    exit 1
fi

hostnamectl set-hostname $hostname
echo "1-Hostname updated"

ip addr show $id_carte_reseau &> /dev/null

if [ $? -ne 0 ]; then
    echo "L'interface $id_carte_reseau n'existe pas"
else
    ip link set $id_carte_reseau down
    
    sudo echo "network:
  ethernets:
    $id_carte_reseau:
      dhcp4: no
      addresses:
        - $address_reseau/28
      gateway4: $address_passerelle
      nameservers:
          addresses: [$address_dns, 1.1.1.1]
  version: 2
    " > /etc/netplan/00-installer-config.yaml
    echo Address updated..............."
    netplan apply
    echo Address applied..............."
    ip a
    ip link set $id_carte_reseau up
    echo "All done"
    while ! ping -c 3 8.8.8.8; do
        sleep 1
    done
fi

exi