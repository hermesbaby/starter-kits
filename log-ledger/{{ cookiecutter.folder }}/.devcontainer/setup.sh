#!/usr/bin/env bash

#############################################################################
#                                                                           #
#   This file is part of hermesbaby - the software engineers' typewriter    #
#                                                                           #
#   Copyright (c) 2024 Alexander Mann-Wahrenberg (basejumpa)                #
#                                                                           #
#   https://hermesbaby.github.io                                            #
#                                                                           #
# - The MIT License (MIT)                                                   #
#   when this becomes part of your software                                 #
#                                                                           #
# - The Creative Commons Attribution-Share-Alike 4.0 International License  #
#   (CC BY-SA 4.0) when this is part of documentation, blogs, presentations #
#                  or other content                                         #
#                                                                           #
#############################################################################

### Enable exit on error ######################################################
set -e

### Update local apt index ####################################################

apt-get update -y

### Make python3 available under name "python" ################################

export DEBIAN_FRONTEND=noninteractive
apt-get install -y   \
   python-is-python3

### Install pip  ##############################################################

curl -sS https://bootstrap.pypa.io/get-pip.py | python


### Install venv  #############################################################

apt-get install -y python3.10-venv


### Install poetry inside pipx ################################################
python -m pip install pipx
python -m pipx install poetry
pipx ensurepath
export PATH="$PATH:$HOME/.local/bin" # Works at least for root. That's fine for docker/devcontainers


### Make available drawio in headless mode ####################################

# Install drawio

if which drawio; then
    echo "drawio is already installed"
else
    drawio_package=drawio-amd64-24.4.13.deb
    curl -L -o $drawio_package https://github.com/jgraph/drawio-desktop/releases/download/v24.4.13/$drawio_package
    apt install -y ./$drawio_package
    rm $drawio_package
fi

# Install virtual X-Server
apt-get install -y xvfb


### Install mermaid command line tool #########################################

# Install nodejs (brings package manager npm with it)
curl -fsSL https://deb.nodesource.com/setup_20.x | bash
apt install -y nodejs

#
npm install -g @mermaid-js/mermaid-cli
mmdc --version

### Reload environment ########################################################

source ~/.bashrc


### EOF #######################################################################

