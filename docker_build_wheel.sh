#!/bin/bash
#set -ex

cd $(dirname "$0")
echo $PWD

cmake --version
more /etc/issue

python setup.py sdist bdist_wheel

#pip wheel --no-deps -w /io/wheelhouse .

#if [ $(uname) == 'Darwin' ]; then
    #for lib in $(find $JSBSIM_PATH/lib -name "*.dylib"); do
        #install_name_tool -id $lib $lib
        ##for dep in $(otool -L $lib | grep "@rpath" | awk '{print $1}'); do
            #install_name_tool -change $dep "$JSBSIM_PATH/lib/${dep##@rpath/}" $lib
        #done
    #done
#fi
#
#if [ $(uname) == 'Linux' ]; then
    #for lib in $(find $JSBSIM_PATH/lib -name "*.so.2.87"); do
        #patchelf --set-rpath $JSBSIM_PATH/lib $lib
    #done
#fi
