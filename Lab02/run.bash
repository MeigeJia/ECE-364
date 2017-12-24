#! /bin/bash

#---------------------------------------
# $Author: ee364c08 $
# $Date: 2017-09-03 18:06:29 -0400 (Sun, 03 Sep 2017) $
#---------------------------------------

# Do not modify above this line.

for file in c-files/*.c
do
	fileName=$(cut -c9- <<< "$file")
	fileName=${fileName%.*}
	printf "Compiling file $fileName... "
	gcc -Wall -Werror "$file" 2> /dev/null 
	if (( $? == 0)); then
		printf "Compilation succeeded.\n"
		./a.out > $fileName.out
	else
		printf "Error: Compilation failed.\n"
	fi
done

exit 0
