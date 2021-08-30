#!/bin/bash
while :
do
    cd /home/james/dev/Python/pybar
    xsetroot -name "$(pipenv run python .)"
    sleep 1
done
