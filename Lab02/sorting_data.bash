#! /bin/bash

#---------------------------------------
# $Author: ee364j02 $
# $Date: 2017-09-05 16:50:38 -0400 (Tue, 05 Sep 2017) $
#---------------------------------------

# Do not modify above this line.

numInputs=$#

if (( $numInputs != 1 ))
then
	echo "Usage: ./sorting_data.bash <input file>"
	exit 1
fi

if ([ ! -r $1 ])
then
	echo "Error! $1 is not a readable file."
	exit 2
fi

echo "Your choices are: "
echo "1) First 10 people"
echo "2) Last 5 names by highest zipcode"
echo "3) Address of 6th-10th by reverse e-mail"
echo "4) First 12 companies"
echo "5) Pick a number of people"
echo "6) Exit"

while (( 1 ))
do
	read -p "Your choice: " choice

	if (( $choice == 1 ))
	then
		tail -n +2 "$1" | sort -t, -k7,7 -k5,5 -k2,2 -k1,1 | head -n 10
	elif (( $choice == 2 ))
	then
		tail -n +2 "$1" | sort -t, -n -k8,8 | tail -n 5 | cut -d, -f2,1
	elif (( $choice == 3 ))
	then 
		tail -n +2 "$1" | sort -t, -r -k11,11 | head -n 10 | tail -n 5 | cut -d, -f4
	elif (( $choice == 4 ))
	then
		tail -n +2 "$1" | sort -t, -k3,3 | head -n 12 | cut -d, -f3
	elif (( $choice == 5 ))
	then
		read -p "Enter a number: " number
		tail -n +2 "$1" | sort -t, -k2,2 -k1,1 | head -n $number
	elif (( $choice == 6 ))
	then
		echo "Have a nice day!"
		break
	else
		echo "Error! Invalid Selection!"
	fi
done

exit 0


