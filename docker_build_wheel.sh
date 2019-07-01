#!/bin/bash
#set -ex

cd $(dirname "$0")

python setup.py sdist bdist_wheel
