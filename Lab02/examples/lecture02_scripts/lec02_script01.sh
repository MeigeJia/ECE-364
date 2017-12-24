#! /bin/bash
# ################################################################
#
#   Arrays
#
# ################################################################

echo "**********************"
echo "Section 1: Arrays"
echo "**********************"

# Create an array from space separated values.
singleVariable="This is a single variable"

# What's in the variable?
echo
echo $singleVariable
echo
# Convert to array.
arrayVariable=($singleVariable)

# Notice the output of the following:
echo "Printing a variable without the [] will give *$arrayVariable*."
echo "-----------------------"
echo "The fourth element of the array is: ${arrayVariable[3]}"
echo "-----------------------"
echo "We have ${#arrayVariable[*]} elements in this array."
echo "-----------------------"
echo "All of the array content is: ${arrayVariable[*]}"
echo "-----------------------"
echo "Indices of the array: ${!arrayVariable[*]}"
echo "-----------------------"

# Let's change one element.
arrayVariable[4]=sentence
echo "Now, we have: ${arrayVariable[*]}"
echo "-----------------------"
echo "-----------------------"
echo

# Get the files and assign them to an array. (Note the quotation!)
nameList=(`ls`) # Or, better yet nameList=($(ls))
echo First File here is \"${nameList[0]}\" # First element
echo "There are ${#nameList[*]} file(s) in this Folder" # Count.

exit 0