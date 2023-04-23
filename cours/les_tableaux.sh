#!/bin/bash

tab=('toto' 'taata' 'SEOSOE')
tab[0]="VOVOV"

echo "${tab[0]}"
echo "${tab[1]}"
# Le @ pour afficher tous les elements du tableaux
echo "${tab[@]}"

# La taille du tableau
echo  "${#tab[*]}"
