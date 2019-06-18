#!/bin/bash
set -ex

rm -rf build dist gym_jsbsim.egg-info
docker run -v $PWD:/io gualleon583a/python:3 /io/docker_build_wheel.sh
