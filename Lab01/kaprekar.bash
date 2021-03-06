#! /bin/bash

#---------------------------------------
# $Author: ee364c08 $
# $Date: 2017-08-29 17:19:45 -0400 (Tue, 29 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

inputNum="$1"
numInputs="$#"

if (( $numInputs != 1 ))
then
	printf "Usage: kaprekar.bash <non-negative integer>\n"
	exit 1
fi

if (( $inputNum >= 1 ))
then
	echo 1, square=1, 1+0=1
fi


for (( i=4 ; i<=inputNum ; i++ ))
do
	num=$i
	let numSq=$num*$num
	len=${#numSq}
	let mp1=($len)/2
	let mp2=$mp1+1
	num1=$(echo $numSq | cut -c 1-$mp1)
	num2=$(echo $numSq | cut -c $mp2-$len)
	let tot=$((10#$num1))+$((10#$num2))

	if (( $tot == $num ))
	then
		echo $num, square=$numSq, $num2+$num1=$tot
	fi
done


exit 0



