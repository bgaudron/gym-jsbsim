FROM ubuntu:16.04
# get dependencies
RUN apt-get -y update && apt-get -y install python3-dev python3-pip curl apt-utils patchelf cmake pkg-config git
# set python and pip to point to python3 versions
RUN bash -c "ln -s $(which python3) /usr/bin/python && ln -s $(which pip3) /usr/bin/pip"
COPY . /code
RUN  cd /code && \
     bash -c ". ./exports.sh && ./install_jsbsim.sh && ./jsbsim_compile_and_graft.sh"

# install pip package and test
RUN pip install -e /code
RUN python -c "import gym; gym.make('roboschool:RoboschoolAnt-v1').reset()"
