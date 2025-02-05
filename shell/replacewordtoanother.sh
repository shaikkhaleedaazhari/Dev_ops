#!/bin/bash
#Author: khaleeda
#purpose: replacewordtoanother
#usage: ./replacewordtoanother.sh
echo "Enter your file"
read -r file
echo "Enter the word to replace"
read -r word
echo "Enter new word"
read -r newword
echo "${file/$word/$newword}"

