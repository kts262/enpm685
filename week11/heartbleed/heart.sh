#!/bin/sh

input=heart.list

while read ip 
do
        ./heart.py $ip -p 443 
done < $input
