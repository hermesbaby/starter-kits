#!/usr/bin/env sh

################################################################
#                                                              #
#  This file is part of hermesbaby                             #
#                       the software engineer's typewriter     #
#                                                              #
#  Copyright (c) 2024 Alexander Mann-Wahrenberg (basejumpa)    #
#                                                              #
#      https://github.com/basejumpa                            #
#                                                              #
#  License(s)                                                  #
#                                                              #
#  - MIT for contents used as software                         #
#  - CC BY-SA-4.0 for contents used as method or otherwise     #
#                                                              #
################################################################

# Usage: ./save_my_day

user=$(whoami)
host=$(hostname)
today=$(date +'%GCW%V.%u_%a' | tr '[a-z]' '[A-Z]')

message="$today $user@$host "

git add .
git commit --message "$message"
git push

