#!/bin/bash

var1=0
echo $var1
let var1++
echo $var1
let var1--
echo $var1

var2=45
var2=$var2+359
echo $var2

var3=4
var3=$((var3+359))
echo $var3

var4=7
#Code dépricier: utiliser avec celui de la variables 3
var4=$[$var4+3]
echo $var4