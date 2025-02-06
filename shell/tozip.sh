#!/bin/sh
# How to zip a folder
echo "Enter the folder name"
read -r foldername

if [ -d "$foldername" ]; then
    zip -r "${foldername}.zip" "$foldername"
    echo "Folder '$foldername' has been zipped into '${foldername}.zip'"
else
    echo "Folder does not exist"
fi