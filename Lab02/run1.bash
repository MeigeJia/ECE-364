#! /bin/bash

for filen in c-files/*.c
do
	temp=${filen/"c-files/"}
	temp=${temp%".c"}
	echo ${temp}
	if gcc -Wall -Werror $filen 2> /dev/null
	then
		echo kk
	else
		echo fail
	fi

done

