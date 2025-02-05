#!/bin/sh
#Author: khaleeda
#purpose: avg
#usage: ./sstudentssavgsh
#math pys chem 35 <
#if not avg > 80 detination
#if avg > 60 1st class
#if avg > 45 nd class
echo "Enter marks for maths"
read -r maths
echo "Enter marks for phy"
read -r phy
echo "enter marks for chemi"
read -r chem

if [ "$maths" -lt 35 ] || [ "$phy" -lt 35 ] || [ "$chem" -lt 35 ]; then
    echo "you are fail"
else
    total=$((maths + phy + chem))
    avg=$((total / 3))
    echo "avg mks $avg"
    if [ $avg -ge 80 ]; then
        echo "dstination"
    elif [ $avg -ge 60 ]; then
        echo "1st class"
    elif [ $avg -ge 45 ]; then
        echo "2nd class"
    fi
fi