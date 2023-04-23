#!/bin/bash

#Extraction chaine: Dans une chainne, à partir d'une position à un nombre définit de caractères
chaine="Salut a vous tous"
chaine2=${chaine:8:4}
echo "$chaine"
echo "$chaine2"

#Troncature: Dans une chaine, un nombre définit de caractères
chaine3=${chaine:6}
echo "$chaine3"


#Notion de séparateur
echo "----------------------Notion de séparateur-------------------------------"
oldIFS=$IFS
toto="diallo;koula;bassirou;toto"
echo "$toto"
echo "*********1*********"
IFS=';'
echo "$toto"
for variable in $toto; do
    echo "$variable"
done
echo "*********2*********"
IFS=$oldIFS
echo "$toto"

echo "----------------------IFS et fichier-------------------------------"
afficher(){
    oldIFS=$IFS
    IFS=';'
    for variable in $1; do
        echo "$variable"
    done
    IFS=$oldIFS
    echo "Done...!-----------"
}

while read -r LINE; do
    afficher "$LINE"
done < mdp.txt



