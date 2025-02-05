#!/bin/sh
#Author: khaleeda
#purpose: creating a variable
#usage: ./variable.sh
file=$1
if [ -f "$file" ]; then
	echo "file exist"
else 
	echo "file not exists"
fi

file=$1
if [[ -f $file ]]; then
	echo "file exist"
else 
	echo "file not exists"
fi