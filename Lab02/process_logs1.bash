#! /bin/bash

numArgs=$#
fileName=$1

if [[ -r "${fileName}" ]]
then
	echo READABLE
fi

count=1
while read line
do
	if (( $count == 1 ))
	then
		count=2
		continue
	fi

	temp1=$(echo ${line} | cut -d" " -f2)
	temp2=$(echo ${line} | cut -d" " -f3)
	temp3=$(echo ${line} | cut -d" " -f4)
	temp4=$(echo ${line} | cut -d" " -f5)
	
	let avg=$temp1+$temp2+$temp3+$temp4
	avg=$(echo "scale=2;$avg/4" | bc)

done < "${fileName}"

count=1
ind=0

exec 4< "${fileName}"
read line <&4
read line <&4

while read line <&4
do
#	if (( $count == 1 ))
#	then
#		count=2
#		continue
#	fi
	#echo $line
	mach1[$ind]=$(echo ${line} | cut -d" " -f2)
	mach2[$ind]=$(echo ${line} | cut -d" " -f3)
	mach3[$ind]=$(echo ${line} | cut -d" " -f4)
	mach4[$ind]=$(echo ${line} | cut -d" " -f5)
	
done


while read line
do
	echo $line
done < "${fileName}" | tail -n +2


