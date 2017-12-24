#! /bin/bash

#---------------------------------------
# $Author: ee364c08 $
# $Date: 2017-08-29 16:59:31 -0400 (Tue, 29 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

fileName="$1"
if [[ "$fileName" == "" ]]
then
	printf "Usage: check_permissions.bash <input file/directory>\n"
	exit 1
fi
string=$(ls -ld $fileName)

ownerPerm=$(echo $string | cut -c 2-4)
groupPerm=$(echo $string | cut -c 5-7)
otherPerm=$(echo $string | cut -c 8-10)

echo Owner Permissions:

readPerm=$(echo $ownerPerm | cut -c1)
writePerm=$(echo $ownerPerm | cut -c2)
execPerm=$(echo $ownerPerm | cut -c3)

if [[ "$readPerm" == "r" ]]
then
	echo "$fileName is readable"
else
	echo $fileName is not readable
fi
if [[ "$writePerm" == "w" ]]
then
	echo $fileName is writeable
else
	echo $fileName is not writeable
fi
if [[ "$execPerm" == "x" ]]
then
	echo $fileName is executable
else
	echo $fileName is not executable
fi

echo
echo Group Permissions:


readPerm=$(echo $groupPerm | cut -c1)
writePerm=$(echo $groupPerm | cut -c2)
execPerm=$(echo $groupPerm | cut -c3)

if [[ "$readPerm" == "r" ]]
then
	echo "$fileName is readable"
else
	echo $fileName is not readable
fi
if [[ "$writePerm" == "w" ]]
then
	echo $fileName is writeable
else
	echo $fileName is not writeable
fi
if [[ "$execPerm" == "x" ]]
then
	echo $fileName is executable
else
	echo $fileName is not executable
fi

echo
echo Others Permissions:


readPerm=$(echo $otherPerm | cut -c1)
writePerm=$(echo $otherPerm | cut -c2)
execPerm=$(echo $otherPerm | cut -c3)

if [[ "$readPerm" == "r" ]]
then
	echo "$fileName is readable"
else
	echo $fileName is not readable
fi
if [[ "$writePerm" == "w" ]]
then
	echo $fileName is writeable
else
	echo $fileName is not writeable
fi
if [[ "$execPerm" == "x" ]]
then
	echo $fileName is executable
else
	echo $fileName is not executable
fi


exit 0
