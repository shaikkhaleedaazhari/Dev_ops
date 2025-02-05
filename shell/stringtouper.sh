#!/bin/sh
#Author: khaleeda
#purpose: stringtoupper
#usage: ./stringtoupper.sh

echo "enter the string"
read -r str
echo "upper string is"
echo "$str" | tr 'a-z' 'A-Z'
