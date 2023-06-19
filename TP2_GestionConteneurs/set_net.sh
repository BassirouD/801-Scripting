#!/bin/bash

# Création de bridge nat

sudo ip link add name br type bridge
sudo ip link set ens33 down
sudo ip addr flush dev ens33
sudo ip link set ens33 up
sudo ip addr add 10.0.2.15/24 broadcast 10.0.2.255 dev br
sudo ip link set dev br up
sudo ip link set ens33 master br
bridge link
sudo ip route add default via 192.168.189.2