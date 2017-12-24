#! /bin/bash
# ################################################################
#
#   I/O Redirection
#
# ################################################################

echo "**********************"
echo "Section 2: I/O Redirection"
echo "**********************"

# Note that the file descriptors 0, 1 and 2 are special. Use with care.
myCommand="ls"

# File descriptor 1 is stdout.
$myCommand >&1

# Create a file for logging.
exec 13>someTextFile.txt

echo This is the beginning of the file >&13
echo ------------------------------------ >&13 
echo $(date) >&13

echo
echo

cat someTextFile.txt

# Send to and read from file.
exec 224>inputParamters.txt
exec 99<inputParamters.txt

echo 13 127 17 >&224

read x y z <&99

echo "Element x is $x"
echo "Element y is $y"
echo "Element z is $z"

# Send to and read from file.
echo Today is Monday >&224
echo Tomorrow is Tuesday >&224
echo

read sentence <&99
echo $sentence
read sentence <&99
echo $sentence

exit 0