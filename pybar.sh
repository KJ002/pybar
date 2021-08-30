#!/bin/bash

cd $HOME/pybar
pipenv sync

while :
do
    xsetroot -name "$(pipenv run python .)"
    sleep 1
done
