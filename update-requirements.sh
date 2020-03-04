#!/usr/bin/env bash

CUSTOM_COMPILE_COMMAND="./update-requirements.sh"
export CUSTOM_COMPILE_COMMAND

pip-compile --annotate --header --upgrade --verbose \
    --output-file requirements.txt requirements.in

safety check --file requirements.txt

