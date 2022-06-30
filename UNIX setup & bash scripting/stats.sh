#!/bin/bash

FILE=${1?Error: Please specify a file to run this Bash script}	# Check if a file has been provided


if [ $(wc -l < $FILE) -lt 10000 ]	# Check if files have atleast 10,000 lines
then
	echo Not enough lines, please input another file
	exit 1
else
	cat $FILE | wc -l	# Number of lines in the file

	head -n 1 $FILE		# Header row
	
	tail -n 10000 $FILE | grep -i "potus" | wc -l	# Number of lines in the last 10,000 rows that had "potus" as a case insensitive string

	awk ' NR >= 100 && NR <= 200' $FILE | grep -w "fake" | wc -l	# Number of lines within lines 100 - 200 containing the case sensitive word "fake"


fi
