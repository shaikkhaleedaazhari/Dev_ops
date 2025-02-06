#!/bin/sh
#entered number is qe hvae to print the fibonaccie series

echo "enter your number"
read -r num
a=0
b=1
for (( i=0; i<num; i++ ))
do 
    echo "$a"
    fn=$((a + b))
    a=$b
    b=$fn
done
