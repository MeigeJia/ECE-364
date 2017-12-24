#! /bin/bash

#----------------------------------
# $Author: ee364c08 $
# $Date: 2017-09-26 16:23:28 -0400 (Tue, 26 Sep 2017) $
#----------------------------------

function part_a 
{               
    # Fill out your answer here
	# Fill out your answer here.
	Arr=(a.txt b.txt c.txt d.txt)
	size=${#Arr[*]}
	echo $( head -n 6 ${Arr[$RANDOM%$size]} | tail -n 3 )
    	return                      
}                               

function part_b
{              
    # Fill out your answer here
	fn=$1
	if [[ -f ${fn} ]]
	then
		echo "$fn is a file name"
	elif [[ -d ${fn} ]]
	then
		echo "$fn is a directory name"
	else
		echo "$fn is not a file name or a directory name"
	fi
    return                     
}                              

function part_c
{
    # Fill out your answer here
	
    return
}

function part_d
{
    # Fill out your answer here
	results=$(wc -wl temp.txt)
	echo $results
	lines=$(echo $results | cut -d" " -f1)
	words=$(echo $results | cut -d" " -f2)
	echo "temp.txt has $words words and $lines lines"
    return
}

function part_e
{
    # Fill out your answer here
	ece364.py &>output.txt
    return
}

function part_f
{
    # Fill out your answer here
	tail -n +2 "people.csv" | sort -t, -k4,4 -k6,6 -k1,1 -k2,2 | tail -n 10 
    return
}

function part_g
{
    # Fill out your answer here
	word="multimillionare"
	len=$(echo $word | wc -c)
	for (( i=1 ; i<=len ; i=i+1 ))
	do
		letter=$(echo $word | cut -c$i)
		if [[ $letter == "a" || $letter == "e" || $letter == "i" || $letter == "o" || $letter == "u" ]]
		then
			let ind=$i-1
			wordList[$ind]="-"
		else
			let ind=$i-1
			wordList[$ind]=$letter
		fi
	done
	echo ${wordList[*]}
    return
}


function part_h
{
    # Fill out your answer here
	for filen in src/*.c
	do
	if gcc -Wall -Werror $filen 2> /dev/null
	then
		echo $filen: success
	else
		echo $filen: failure
	fi

done
    return
}

function part_i
{
    # Fill out your answer here
	grep -c "PURDUE" info.txt
    return
}

function part_j
{
    # Fill out your answer here
	echo $(ping -c3)
    return
}

# To test your function, you can call it below like this:
#
# part_a
part_a
part_b "labfiles"
part_d
part_e
part_f
part_g
part_h
part_i
