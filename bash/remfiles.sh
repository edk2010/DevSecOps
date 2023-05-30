#!/bin/bash
if [[ $1  ]]
then
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
else
	printf "\n\n"
	echo please provide parameter
	printf "\n\n"
	echo ===================================================
	echo usage :
	echo		remfiles [num of characters in file name]
	echo ====================================================
fi
