#!/bin/bash

# Clean data :
#	- delete not "recoded" files
#	- delete empty line in "recoded" files
#	- delete old "recoded" files
for i in $(ls);
do
	for j in $(ls $i);
	do
		if [[ $j =~ [0-9]\.recoded ]] ;
		then
			sed '/^$/d' $i/$j > $i/clear_$j;
			rm $i/$j;
		else
			
			rm $i/$j;
		fi
	done
done

