#! /bin/bash

echo
echo "---------------------------------"
echo

echo "First File Content: "
echo "--------------------"
cat languages1.txt
echo

echo "Second File Content: "
echo "--------------------"
cat languages2.txt
echo

# Combine the files.
cat -n languages1.txt languages2.txt > allLanguages.txt

echo "Combined Content: "
echo "--------------------"
cat allLanguages.txt
echo

# Show selective lines.
head -n 3 allLanguages.txt
echo

tail -n 5 allLanguages.txt
echo

wc -l allLanguages.txt
wc -w allLanguages.txt
wc -c allLanguages.txt
echo
wc allLanguages.txt

# Head and tail.
head -n 10 allLanguages.txt | tail -n 3


exit 0