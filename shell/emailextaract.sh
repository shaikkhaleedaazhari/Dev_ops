#!/bin/bash
#Author: khaleeda
#purpose: emailextract
#usage: ./emailextract.sh
email=$1
if [ ! -f "$email" ]; then
    echo "File not found"
    exit 2
fi
grep -E -o "[A-Za-z0-9.]+@[A-Za-z]+.[A-Za-z]+" "$email"
