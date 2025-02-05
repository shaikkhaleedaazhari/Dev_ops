#!/bin/sh
#Author: khaleeda
#purpose: linux in shell
#usage: ./getopsexam.sh

while getopts :a:b: flag; do
    case $flag in
        a) ab=$OPTARG;;
        b) bc=$OPTARG;;
        ?) echo "i dont undertsand this value"
        esac

        
done
echo "first value $ab, sechond value $bc"