#!/bin/sh
#odd or even 
echo "Enter a number"
read -r num
if [ $((num % 2)) -eq 0 ]; then
    echo "this is even"
else
    echo "this is odd"
fi

#entered nuber is banonaice or not