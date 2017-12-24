#! /bin/bash

# ############################################################################
#
#   Loops
#
# ############################################################################

echo
echo
echo "---------------------------------"

read -p "Enter max number of lines: " maxValue 

for ind in {1..100}
do
    if (($maxValue < $ind))
    then
        echo
        echo "    Breaking the loop"
        break
    fi

    echo ${ind}
done


exit 0