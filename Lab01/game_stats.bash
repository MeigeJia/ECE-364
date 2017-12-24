#! /bin/bash

#---------------------------------------
# $Author: ee364c08 $
# $Date: 2017-08-27 16:12:20 -0400 (Sun, 27 Aug 2017) $
#---------------------------------------

# Do not modify above this line.


numPlayers=0
numHours=0
maxHours=0
minHours=0

numInputs="$#"
gameName="$2"
dataFile="$1"


if (( $numInputs != 2 ))
then
	echo Error: Insufficient Inputs!
	exit 1
fi

if [[ ! -e $dataFile ]]
then
	echo Error: $dataFile does not exist
	exit 1
fi


while read p; do
	IFS=',' read -ra playerData <<< "$p"
	name="${playerData[0]}"
	game="${playerData[1]}"
	hours="${playerData[2]}"
	
	if([ "$game" == "$gameName" ])
	then
		let numPlayers=$numPlayers+1
		let numHours=$numHours+$hours

		if(( $minHours == 0 || $minHours >= $hours))
		then
			let minHours=$hours
			minPlayer=$name
		fi

		if(( $maxHours == 0 || $maxHours < $hours))
		then
			let maxHours=$hours
			maxPlayer=$name
		fi
	fi

done < $dataFile

printf "Total students: $numPlayers\n"
printf "Total hours spent in a day: $numHours\n"
printf "$maxPlayer spent the highest amount of time in a day: $maxHours\n"
printf "$minPlayer spent the least amount of time in a day: $minHours\n"

