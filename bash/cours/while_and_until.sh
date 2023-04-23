#!/bin/bash

cpt=0
while [ $cpt -le 10 ]; do
    echo "Encore 1: $cpt"
    let cpt++
done

echo "******************** $cpt *********************"

cpt2=0
until [ $cpt2 -eq 10 ]; do
    echo "Encore 1: $cpt2"
    let cpt2++
done