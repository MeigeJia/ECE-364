#! /bin/bash

#---------------------------------------
# $Author: ee364c08 $
# $Date: 2017-08-27 16:12:20 -0400 (Sun, 27 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

hello(){
	printf "Hello "
	whoami
}

quit(){
	printf "Goodbye\n"
	exit 0
}

compile(){
	for fileToCompile in *.c
	do
		curFile=${File%.c}
		if gcc -Wall -Werror ${fileToCompile} -o ${curFile}.o
		then
				printf "Compilation succeeded for: ${fileToCompile} \n"
		else
				printf "Compilation failed for: ${fileToCompile} \n"
		fi
	done
}

whereami(){
	pwd
}

while :
do
	printf "Enter a command: "
	read input

	if([ $input == "hello" ])
	then
		hello
	elif([ $input == "quit" ])
	then
		quit
	elif([ $input == "compile" ])
	then
		compile
	elif([ $input == "whereami" ])
	then
		whereami
	else
		printf "Error: unrecognized input\n"
	fi

	printf "\n"
done




