#!/usr/bin/env bash
set -o errexit  # exit on first error
set -o nounset  # don't allow use of unset variables
set -o pipefail  # produce a failure return code if any pipeline command errors
shopt -s failglob  # cause globs that don't get expanded to cause errors

echo "before_install script"
echo
echo "TRAVIS_BUILD_NUMBER: ${TRAVIS_BUILD_NUMBER}"
echo "TRAVIS_JOB_NUMBER: ${TRAVIS_JOB_NUMBER}"
echo "TRAVIS_OS_NAME: ${TRAVIS_OS_NAME}"
echo "TRAVIS_BRANCH: ${TRAVIS_BRANCH}"
echo "TRAVIS_COMMIT: ${TRAVIS_COMMIT}"
echo "TRAVIS_COMMIT_MESSAGE: ${TRAVIS_COMMIT_MESSAGE}"
echo "TRAVIS_COMMIT_RANGE: ${TRAVIS_COMMIT_RANGE}"
echo "TRAVIS_PULL_REQUEST: ${TRAVIS_PULL_REQUEST}"
echo "TRAVIS_PULL_REQUEST_BRANCH: ${TRAVIS_PULL_REQUEST_BRANCH}"
echo "TRAVIS_EVENT_TYPE: ${TRAVIS_EVENT_TYPE}"
echo "TRAVIS_PYTHON_VERSION: ${TRAVIS_PYTHON_VERSION:-unset}"
echo "VIRTUAL_ENV: ${VIRTUAL_ENV:-unset}"
echo "date: $(date --iso-8601=seconds)"
echo "pwd: $(pwd)"
echo "uname: $(uname --all)"
git --version
echo "git tag: $(git describe --always)"
git config --global user.email "travis@travis.ci"  # overcommit Author
git config --global user.name "Travis CI"  # overcommit Author
git config --global hooks.copyrightholder "Francis T. O'Donovan"
echo "python version: $(python --version)"
shellcheck --version
ruby --version
gem update --system --no-document
gem --version
npm --version
echo "disk usage:"
df --human-readable
