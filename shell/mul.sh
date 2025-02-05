#!/bin/sh
#Author: khaleeda
#purpose: leaning while loop 
#usage: ./mul.sh
echo "Provide the number"
read -r no
echo "mul of $no"
counter=1
while [ $counter -le 10 ]
do
	mult=`expr $no \* $counter`
	echo "$no * $counter = $mult"
	counter=$(expr $counter + 1)
done
