#!/bin/bash

# compile
pyinstaller ~/source/todo-line/src/todo.py --onedir

echo 'Deleting existing....'
# delete existing files
rm -rf ~/Applications/todoline/*
echo 'Deletion finished.'

echo 'Deploying update application....'
# copy to location
cp -r ~/source/todo-line/dist/todo/. ~/Applications/todoline
echo 'Deployment successful.'
