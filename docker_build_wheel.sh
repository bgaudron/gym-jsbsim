#!/bin/bash
set -ex
apt-get update && apt-get install -y patchelf cmake > /dev/null

cd $(dirname "$0")
. ./exports.sh

./install_jsbsim.sh
./jsbsim_compile_and_graft.sh

pip wheel --no-deps -w /io/wheelhouse .
