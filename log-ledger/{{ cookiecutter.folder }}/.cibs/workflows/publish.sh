#!/usr/bin/env bash

### THIS SCRIPT EXPECTS THAT IT'S CWD IS THE WORKSPACE ROOT FOLDER ###

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

echo ## CONFIGURATION ####################################################

CFG_WORKFLOW_LOG_DIR=out/


echo ## PREPARATIONS #####################################################

# Enable printing of the commands themselves
set -x

# Write output of any subsequent commands also into the log file
mkdir -p $CFG_WORKFLOW_LOG_DIR
exec > >(tee "$CFG_BUILD_OUT_PATH/$(basename $0).log") 2>&1

# Enable exit on error
set -e

echo ## WORKFLOW #########################################################

## Git out of detached HEAD state. Jenkins has set environment variable "branch" to the branch name.
git checkout $branch

## Generate and publish the documentation
make -f docs/Makefile publish-on-ci


echo ## END OF WORKFLOW ################################################

exit 0
