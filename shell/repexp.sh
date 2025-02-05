#!/bin/sh
#Author: khaleeda
#purpose: repural expression
#usage: ./repexp.sh

numstring="123456789"
if [[ $numstring =~ ^1 ]]; then
    echo "$numstring starts with 1"
fi

numstring="ABCDabcd"
if [[ $numstring =~ ^[A-Za-z]+$ ]]; then
    echo "$numstring starts with a and z presnt"
fi
#[]--is used in bash
#[[]]--no need of adding quotes...for example file having spcae in name
# then we have to give quotes and all..so we can keep [[]] instead of []
# ^--means startung with
# . --means any character
# if [[ $numstring =~ 8$ ]]; then---fo find the ending with 8 or not
# if [[ $numstring =~ [0-9]$ ]]; then---to find the ending with any number


#math pys chem 35 <
#if not avg > 80 detination
#if avg > 60 1st class
#if avg > 45 end class