#!/bin/bash

echo "START"
python3 "${1}.py"	

for (( ; ; ))
do
	read -p "RESTART? [y/n] :" word
	if [[ "$word" == "n" ]];then
		exit 0
	else 
		python3 "${1}.py"
	fi
done
