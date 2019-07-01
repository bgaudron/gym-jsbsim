FROM ubuntu:19.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y patchelf curl git python3-dev python3-pip cython3 cmake
RUN bash -c "ln -s $(which python3) /usr/bin/python && ln -s $(which cython3) /usr/bin/cython && ln -s $(which pip3) /usr/bin/pip"
