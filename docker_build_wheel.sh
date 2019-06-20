#!/bin/bash
#set -ex

cd $(dirname "$0")
echo $PWD

python setup.py sdist bdist_wheel

#pip install gym

#pip wheel --no-deps -w /io/wheel_house .
pip install dist/gym_jsbsim-1.0.0-cp36-cp36m-linux_x86_64.whl

ls -lrt /usr/lib/python3.*/site-packages/gym_jsbsim/

#python test_agent.py

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
