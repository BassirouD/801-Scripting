#!/bin/bash

#1) Rédirection dans un fichier en écrivant dedans
list=$(ls)
for element in $list; do
    echo "$element" >> toto.txt
done


#2) Lecture d'un fichier
    #- La redirection
list=$(<toto.txt)
for element in $list; do
    echo "$element" >> toto2.txt
done

    #- Le cat
list=$(cat toto.txt)
for element in $list; do
    echo "$element" >> toto3.txt
done

#3) Lecture ligne a ligne
cpt=1
while read LINE; do
    echo $cpt ":" "$LINE"
    let cpt++
done < toto3.txt