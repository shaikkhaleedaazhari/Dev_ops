#before 12 good morning
#after 12 to 4 good afternoon
#after 4 to 8 good evening
#after 8 good night
#!/bin/sh
#Author: khaleeda
#purpose: linux in shell
#usage: ./clock.sh
date=`date`
h=$(date +"%H")

if [ $h -le 12 ]; then
    echo "hey good morning"
elif [ $h -le 16 ]; then
    echo "hey good after"
elif [ $h -le 20 ]; then
    echo "hey good evening"
else
    echo "hey good night"
fi