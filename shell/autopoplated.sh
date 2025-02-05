#!/bin/sh
#Author: khaleeda
#purpose: autopoplated
#usage: ./autopoplated.sh

echo "All the arguments are included here  $*"
echo "Number of arguents $#"
echo "third $1"
echo "split word form or expand and the argumenst as seperate words $@"
echo "process id of the current process $$"

sleep 400 &
echo "process id of recently background $!"
echo "current file name $0"

