#! /bin/bash

# $Author: ee364j02 $
# $Date: 2017-09-05 16:50:38 -0400 (Tue, 05 Sep 2017) $

function array 
{
    # Fill out your answer here.
	Arr=(a.txt b.txt c.txt d.txt e.txt)
	size=${#Arr[*]}
	head -n 9 ${Arr[$RANDOM%$size]} | tail -n 3
    return

}

array
exit 0
#
# To test your function, you can call it below like this:
#
#array
#
