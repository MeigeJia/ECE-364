#! /bin/bash

fileName=$1
outName=$2

count=1

>$outName

while read line
do
	if (( $count == 1 ))
	then
		mach1=$(echo $line | cut -d" " -f2)
		mach2=$(echo $line | cut -d" " -f3)
		mach3=$(echo $line | cut -d" " -f4)
		mach4=$(echo $line | cut -d" " -f5)
		count=2
		continue
	fi
	time=$(echo ${line} | cut -d" " -f1)
	temp1=$(echo ${line} | cut -d" " -f2)
	temp2=$(echo ${line} | cut -d" " -f3)
	temp3=$(echo ${line} | cut -d" " -f4)
	temp4=$(echo ${line} | cut -d" " -f5)	

	echo "$mach1,$time,$temp1" >> $outName
	echo "$mach2,$time,$temp2" >> $outName
	echo "$mach3,$time,$temp3" >> $outName
	echo "$mach4,$time,$temp4" >> $outName

done < $fileName

sort -t"," -k3,3r -k1,1 -o "RESULTS.txt" $outName

