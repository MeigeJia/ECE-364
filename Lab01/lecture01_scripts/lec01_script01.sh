#! /bin/bash

# ############################################################################
#
#   This is a common way of commenting in Bash, where the comments are boxed
#   to give a quick clue of the beginning of a script.
#   
#   Author:     <Something goes here!>
#   Purpose:    <Something else goes here!>
#   Date:       <You got the point!>
#   ...
# ############################################################################

# NOTE: First, run the script, then try with debug -x turned on.
# ./lec01_script01.sh I_am_input_1 01-14-2014 somethingElse

echo
echo

# Use the special variables directly.
echo "We are living in Process ID = $$."
echo "---------------------------------"

# Working with a variable that does NOT exist
echo "The invisible variable = $iDoNotExist"

# Use the special variable via assignment.
inputParameterCount=$#
inputParameters=$@

# Show some input parameters.
echo
echo "You passed in $inputParameterCount, and they are: \"$inputParameters\""
echo "First Input: \"$1\""
echo "Second input: \"$2\""
echo "---------------------------------"

# Check return codes.
echo
echo "Previous return code = $?"

/bin/bash dummyScriptThatReturns42.sh

echo "Trying return code again = $?"

# Some maths operations.
foo=$RANDOM
bar=$RANDOM

let productOfTwo=(foo*bar)

echo
echo "---------------------------------"
echo "We began with $foo & $bar. The sum = $((foo + bar)) and the product \
= ${productOfTwo}."

# The $(...) and the backslash will be covered later, but just try them out.
currentFolder=$(pwd)
echo "Current working Directory is \"${currentFolder}\""
echo

exit 0