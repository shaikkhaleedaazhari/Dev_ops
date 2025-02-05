#!/bin/sh
echo "this is for shell script"
#Author: khaleeda
#purpose: creating a variable
#usage: ./variable.sh
var1=10
var2="Hello"
myhostname=$(hostname)
date=`date`
#the folowing variable defination are not allowed
1value=100
false@linux=false
echo "var1=$var1"
echo "var2=$var2"
echo "hostname=${myhostname}"
echo "date=$date"
echo "1value=$1value"
echo "false@linux=$false@linux"

