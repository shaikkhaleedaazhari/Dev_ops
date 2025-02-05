#!/bin/sh
#Author: khaleeda
#purpose: learning function
#usage: ./functionwithparathesis.sh
function sum
{
        local total=$(( $1 +$2))
        echo "$total"
}
echo "Enter first number"
read num1
echo "enter scound number"
read num2

sum $num1 $num2