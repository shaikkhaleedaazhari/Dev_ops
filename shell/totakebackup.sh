#!/bin/sh
#Author: khaleeda
#purpose: learning function
#usage: ./totakebackup.sh
function backup {
    echo "enter the file name to take backup"
    read -r myfile
    # if [ -f $myfile ]; then
    #     echo "file exist"
    #     echo "taking backup"
    #     cp $myfile /tmp/backup
    # else
    #     echo "file does not exist"
    # fi
    # if [ $? -ne 0]; then
    #     echo "failed backup $?"
    # fi
    cp $myfile /tmp/backup
     echo $?
    if [ $? -ne 0 ]; then
        echo "failed backup $?"
    fi
}
backup


#Why $?
# Hence check the file once more