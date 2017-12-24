#! /bin/bash

# ############################################################################
#
#   Conditional Testing
#
# ############################################################################

echo
echo
echo "---------------------------------"

firstValue=$RANDOM
secondValue=$RANDOM

echo "First Number = $firstValue, Second Number = $secondValue."
echo

# Check on some conditions.
(($firstValue > $secondValue))
result1=$?

(($firstValue < $secondValue))
result2=$?

echo "Results of comparison are \"$result1\" and \"$result2\"."

# Try the if statement.
if (($firstValue > $secondValue))
then
    echo
    echo "    First result is true. Its value = \"$result1\""
    echo
    # Note the space before and after the '!'
elif (( ! $firstValue > $secondValue ))
then
    echo
    echo "    Second result is true. Its value = \"$result2\""
    echo
fi

testFile=lec01_script01.sh

echo "---------------------------------"
echo

# Continue to execute the second part "if and only if" the first is FALSE
[[ -e $testFile ]] && echo "File exists."
[[ -e $testFile ]] || echo "File does NOT exist."

[[ -d $testFile ]] && echo "This is a directory."
[[ -d $testFile ]] || echo "This is NOT a directory."

[[ -x $testFile ]] && echo "File is executable."
[[ -x $testFile ]] || echo "File is NOT executable."

echo
echo "---------------------------------"
echo

# Note that for strings, the equality check can be '=' or '=='
if [[ "0" = "1" ]]
then
    echo True
elif [[ "0" != "1" ]]
then
    echo False
fi

exit 0