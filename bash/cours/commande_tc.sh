#!/bin/bash

#Ajout d'un delai constant a une interface
#Tester avec ping sur 8.8.8.8
sudo tc qdisc add dev ens33 root netem delay 100ms

#Suppression du delai
sudo tc qdisc del dev ens33 root