#!/bin/bash

str=$(date +%H%M)

for ((num=0; num<${#str}; num++ ))
do 
	aplay -q /home/galvanix/Documents/git/timecode/wav/${str:num:1}.wav 
	if [ $num -eq 1 ]
		then
			aplay -q /home/galvanix/Documents/git/timecode/wav/wordspace.wav
	fi
done
