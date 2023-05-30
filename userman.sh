#!/bin/bash

promt="users>"

while [[ $cmd != "exit" ]]
do
    printf "%s" $promt
    read -a cmd
    case ${cmd[0]} in

        find)
                count=0
                myfiles=($(ls *.user))
                for myfile in ${myfiles[@]}
                do
                        #echo  $myfile
                        if [[ $myfile = ${cmd[1]}.user  ]]
                        then
                                cat $myfile
                                let "count += 1"
                        fi


                    done

                if [[ $count = 0 ]]
                then
                                #echo count $count
                                printf "No user %s \n"  ${cmd[1]}
                fi
        ;;
        list)
                count=0
                myfiles=($(ls *.user))
                for myfile in ${myfiles[@]}
                do
                let "count += 1"
                echo $myfile | cut -d "." -f1
                done
                if [[ $count = 0 ]]
                then
                        echo no users to display
                fi
        ;;
        del)
                if [[ -f "${cmd[1]}.user"  ]]
                then
                        rm ${cmd[1]}.user &>/dev/null
                        echo user ${cmd[1]} deleted
                else
                        echo user ${cmd[1]} not exist
                fi

        ;;


        new)
                touch ${cmd[1]}.user
                echo name: ${cmd[1]} > ${cmd[1]}.user
                echo password: $RANDOM >> ${cmd[1]}.user
                printf "Created user %s \n" ${cmd[1]}
        ;;
    esac


done

printf "\n\n"
echo +++++++++++
echo + GoodBye +
echo +++++++++++
printf  "\n\n"
