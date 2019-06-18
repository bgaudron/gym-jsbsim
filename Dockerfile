FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y patchelf curl git python3-dev python3-pip cython3 cmake
RUN bash -c "ln -s $(which python3) /usr/bin/python && ln -s $(which cython3) /usr/bin/cython && ln -s $(which pip3) /usr/bin/pip"
#COPY . /code
#RUN  cd /code && \
#     bash -c ". ./exports.sh && ./install_jsbsim.sh && ./jsbsim_compile_and_graft.sh"
#
# install pip package and test
#RUN pip install -e /code
#RUN python -c "import gym; gym.make('roboschool:RoboschoolAnt-v1').reset()"
