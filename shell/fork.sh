#!/bin/sh
#Author: khaleeda
#purpose: leaning for loop 
#usage: ./variable.sh
fruits=("apple" "banana" "jackfruits")
for fruit in "${fruits[@]}"; do 
	echo "i like to eat $fruit"
done

fruits=("apple" "banana" "jackfruits")
for i in "${!fruits[@]}"; do 
	echo "fruit at $i is ${fruits[$i]}"
done

fruits=("apple" "banana" "jackfruits" "mango")
for i in "${!fruits[@]}"; do 
	if((i%2==0)); then
		echo "$i I like fruits ${fruits[$i]}"
	else
		echo "$i I dont like fruit ${fruits[$i]}"
	fi
done

fruits=("apple" "banana" "jackfruits" "mango")
for i in "${!fruits[@]}"; do
	if((i%2!=0)); then
		echo "$i fruits are ${fruits[$i]}"
	fi
done

shaikka@gmail.com