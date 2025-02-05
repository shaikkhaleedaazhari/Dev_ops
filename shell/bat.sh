#!/bin/sh
#Author: khaleeda
#purpose: creating a batman
#usage: ./bat.sh
echo "Enter the batman score"
read -r no
if [ "$no" -le 20 ]; then
	echo "batman not scored well"
elif [ "$no" -ge 20 ] && [ "$no" -le 60 ]; then
	echo "batman scored well"
else
	echo "batman scored super"
	fi


for i in 1 2 3 4 5
do 
	echo "$i"
done

for i in {1..5};
do
	echo "$i"
done

for i in $(seq 1 5);
do
	echo "$i"
done

for ((i=1;i<=10; i++ ));
do
	echo "$i"
done