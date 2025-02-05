#write a shell script to clone a git repo and deploy maven ased java applicatio in tomcat.
#1. Download tomat and unzip webapps bin

#2. write shell scripyt
# input : git repo
# clone the repo
# get inside
# mvn clean package
# target folder--warfile
# copy * .war to webapps of tomat
# $tomcat/bin/catlina.sh start