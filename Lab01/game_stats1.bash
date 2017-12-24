#! /bin/bash

numInputs=$#
fileName=$1
gameName=$2

#echo $numInputs, ${fileName}, ${gameName}

if [[ -e ${fileName} ]]
then
	echo exists
else
	echo nope
	exit 2
fi

totPlayers=0
while read line
do
	curGame=$(echo ${line} | cut -d"," -f2)
	if [[ "${curGame}" == "${gameName}" ]]
	then
		let totPlayers=totPlayers+1
	fi
done < $1

echo $totPlayers



