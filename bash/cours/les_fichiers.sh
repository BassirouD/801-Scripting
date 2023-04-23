#!/bin/bash

#Rédirection dans un fichier en écrivant dedans
list=$(ls)
for element in $list; do
    echo "$element" >> toto.txt
done



