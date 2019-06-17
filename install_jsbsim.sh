#!/bin/bash

JSBSIM_SRCDIR=$(mktemp -d)/jsbsim
JSBSIM_PATH=$HOME/.forked_jsbsim

rm -rf $JSBSIM_SRCDIR
mkdir -p $JSBSIM_SRCDIR && cd $JSBSIM_SRCDIR
git clone https://github.com/JSBSim-Team/jsbsim.git .

mkdir build && cd build
cmake -DCMAKE_CXX_FLAGS_RELEASE="-O3 -march=native -mtune=native" -DCMAKE_C_FLAGS_RELEASE="-O3 -march=native -mtune=native" -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=ON -DINSTALL_PYTHON_MODULE=ON

make -j4 > /tmp/jsbsim_make.log || (tail -100 /tmp/jsbsim_make.log; exit 1)
make install > /tmp/jsbsim_install.log || (tail -100 /tmp/jsbsim_install.log; exit 1)

if [ $(uname) == 'Darwin' ]; then
    for lib in $(find $JSBSIM_PATH/lib -name "*.dylib"); do
        install_name_tool -id $lib $lib
        for dep in $(otool -L $lib | grep "@rpath" | awk '{print $1}'); do 
            install_name_tool -change $dep "$JSBSIM_PATH/lib/${dep##@rpath/}" $lib
        done
    done
fi

if [ $(uname) == 'Linux' ]; then
    for lib in $(find $JSBSIM_PATH/lib -name "*.so.2.87"); do
        patchelf --set-rpath $JSBSIM_PATH/lib $lib
    done
fi
