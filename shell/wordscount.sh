#!/bin/bash
#Author: khaleeda
#purpose: wordscount
#usage: ./wordscount.sh
echo "Enter your string"
read -r str
wd_cnt=$(echo "$str" | wc -w)
echo "Tnumber of words: $wd_cnt" 
