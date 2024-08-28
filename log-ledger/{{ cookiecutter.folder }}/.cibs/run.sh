#!/usr/bin/env bash

## Get out of detached HEAD state. Jenkins has set environment variable "branch" to the branch name.
git checkout $branch

## Installations which will be moved to the Dockerfile
source ./.devcontainer/setup.sh

## Call of the actual workflow script
source ./.cibs/workflows/publish.sh
