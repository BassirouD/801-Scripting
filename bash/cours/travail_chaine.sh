#!/bin/bash

#Extraction chaine: Dans une chainne, à partir d'une position à un nombre définit de caractères
chaine="Salut a vous tous"
chaine2=${chaine:8:4}
echo "$chaine"
echo "$chaine2"

#Troncature: Dans une chaine, un nombre définit de caractères
chaine3=${chaine:6}
echo "$chaine3"
