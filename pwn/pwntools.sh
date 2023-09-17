#!/bin/bash

sudo apt update
sudo apt install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential -y
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools
sudo apt install software-properties-common
sudo apt-add-repository ppa:pwntools/binutils
sudo apt update
sudo apt install binutils -y
