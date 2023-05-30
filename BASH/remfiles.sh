#!/bin/bash

myfiles=($(ls))

for myfile in ${myfiles[@]}
  do
    if [ ${#myfile} = $1 ]
    then
        printf "removing file : %s\n"  $myfile
        #echo ${#myfile}
        rm $myfile
    fi
 done
 
