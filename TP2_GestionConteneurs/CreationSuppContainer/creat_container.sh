#!/bin/bash

nomContainer=$1
nomTemplate=$2
nomDist=$3
architecture=$4
memoire=53687091

sudo DOWNLOAD_KEYSERVER="pgp.mit.edu" lxc-create -t download -n "$nomContainer" -- -d "$nomTemplate" -r "$nomDist" -a "$architecture"

netword_addr=$6
sudo truncate -s 0 /var/lib/lxc/"$nomContainer"/config

echo "

#Distribution config
lxc.include = /usr/share/lxc/config/common.conf
lxc.arch = linux64

#Container specifique config
lxc.rootfs.path dir:/var/lib/lxc/$nomContainer/rootfs
lxc.uts.name = $nomContainer

#Network  config
lxc.net.0.type = veth
lxc.net.0.link = br
lxc.net.0.flags = up
lxc.net.0.veth.pair = br-$nomContainer
lxc.net.0.ipv4.address = $netword_addr

lxc.cgroup.memory.limit_in_bytes = $memoire

" >> /var/lib/lxc/"$nomContainer"/config

exit 0