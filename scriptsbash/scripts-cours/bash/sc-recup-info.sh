#!/bin/bash

compteur=0

while [ -e information$compteur.txt ]; do
    let compteur++
done

touch information$compteur.txt

result=$(id)

echo $result >> ./information$compteur.txt

echo $result

exit 0