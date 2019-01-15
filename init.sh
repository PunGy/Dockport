#!/usr/bin/env bash

if [[ $(whoami) != "root" ]]
then
    echo "You should use sudo before!"
    exit
fi
cp dockport.py /usr/local/bin/dockport
echo "done"