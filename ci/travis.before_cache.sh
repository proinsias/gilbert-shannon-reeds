#!/usr/bin/env bash
set -o errexit  # exit on first error
set -o nounset  # don't allow use of unset variables
set -o pipefail  # produce a failure return code if any pipeline command errors
set -o xtrace  # echo commands
shopt -s failglob  # cause globs that don't get expanded to cause errors

rm --force "${HOME}/.cache/pip/log/debug.log"
