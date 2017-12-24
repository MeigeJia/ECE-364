#! /bin/bash

compile(){
	for file in *.c
	do
		curFile=${file%.c}
		echo ${curFile}
		if gcc -Wall -Werror ${file} -o ${file}.o
		then
			echo "works"
		else
			echo "failed"
		fi
	done
}

compile

