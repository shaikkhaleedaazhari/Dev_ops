#!/bin/bash
#Author: khaleeda
#purpose: Checkpalindrome
#usage: ./stringpalindrome.sh 

echo "Enter your string:"
read -r str
reverse_str=""
len=${#str}

for (( i=$len-1; i>=0; i-- )); do
    # echo "${str:$i:2}"
    reverse_str="$reverse_str${str:$i:1}"
done
echo "$reverse_str"

if [ "$str" = "$reverse_str" ]; then
    echo "The string is a palindrome"
else
    echo "The string is not a palindrome"
fi

