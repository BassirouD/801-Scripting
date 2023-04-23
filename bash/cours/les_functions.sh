#!/bin/bash

#Déclaration
listFic(){
    echo "La liste des fichiers est: "
    ls -l
}

#Appel à la function
listFic

echo "*******************************************"

#Utilisation de parametres
listFile(){
    echo "La liste des fichiers est: "
    ls -l "$1"
}

echo "Donnez le chemin à explorer: "
read -r path
listFile "$path"
