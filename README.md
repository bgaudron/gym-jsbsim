[![Build Status](https://travis-ci.org/galleon/gym-jsbsim.svg?branch=new_gal)](https://travis-ci.org/galleon/gym-jsbsim)


NEWS
====

**2019 June 17, Version 0.1**

* All envs version bumped to “-v1", due to stronger stuck joint punishment, that improves odds of getting a good policy.
* Flagrun-v1 is much more likely to develop a symmetric gait,
* FlagrunHarder-v1 has new "repeat-underlearned" learning schedule, that allows it to be trained to stand up, walk and turn without falling. 
* Atlas robot model, modified (empty links removed, overly powerful feet weakaned).
* All -v1 envs are shipped with better zoo policies, compared to May versions.
* Keyboard-controlled humanoid included.


gym-jsbsim
==========

Release blog post is here:

https://blog.openai.com/roboschool/


Gym-jsbsim is a long-term project to create simulations useful for research. The roadmap is as follows:

1. 
2. 
3. 
4. 
5. 


Some wiki pages:

[Contributing New Environments](https://github.com/galleon/gym-jsbsim/wiki/Contributing-New-Environments)

[Help Wanted](https://github.com/galleon/gym-jsbsim/wiki/Help-Wanted)



Environments List
=================

The list of Roboschool environments is as follows:

- RoboschoolInvertedPendulum-v0

To obtain this list: `import roboschool, gym; print("\n".join(['- ' + spec.id for spec in gym.envs.registry.all() if spec.id.startswith('Roboschool')]))`.


Basic prerequisites
===================
Roboschool is compatible and tested with python3 (3.5 and 3.6), osx and linux. You may be able to compile it with python2.7 (see Installation from source),
but that may require non-trivial amount of work. 

Installation
============

If you are running Ubuntu or Debian Linux, or OS X, the easiest path to install roboschool is via pip (:
```bash
pip install roboschool
```
Note: in a headless machine (e.g. docker container) you may need to install graphics libraries; this can be achieved via `apt-get install libgl1-mesa-dev`

If you are running some other Linux/Unix distro, or want the latest and the greatest code, or want to tweak the compiler optimization options, read on...

Installation from source
========================

Prerequisites
-------------
First, make sure you are installing from a github repo (not a source package on pypi). That is, clone this repo and cd into cloned folder:
```bash
git clone https://github.com/galleon/gym-jsbsim && cd gym-jsbsim
```

The system-level dependencies of gym-jsbsim are cmake.
Linux-based distros will need patchelf utility to tweak the runtime paths. 

- Ubuntu / Debian: 

    ```bash
    sudo apt-get install cmake patchelf
    ```

- OSX:
    
    ```bash
    brew install cmake
    ```

To summarize, all the prerequisites can be installed as follows:
- Ubuntu / Debian: 

    ```bash
    sudo apt-get install patchelf cmake
    ./install_jsbsim.sh
    source exports.sh
    ```

- OSX:
    
    ```bash
    brew install cmake
    ./install_bullet.sh
    source exports.sh
    ```
Now we are ready to compile the gym-jsbsim project itself.

Compile and install
-------------------
The compiler options are configured in the [Makefile](gym-jsbsim/cpp-household/Makefile). Feel free to tinker with them or leave those as is. To
compile the project code, and then install it as a python package, use the following:
```bash
cd gym-jsbsim/cpp-household && make clean && make -j4 && cd ../.. && pip install -e .
```

A simple check if resulting installation is valid:
```python
import gym-jsbsim
import gym

env = gym.make('GymJsbsim-HeadingControlTask-{aircraft_name}-v0')
while True:
    env.step(env.action_space.sample())
    env.render()
```
You can also check the installation running a pretrained agent from the agent zoo, for instance:
```bash
python agent_zoo/tadadam.py
```

Troubleshooting
---------------

Agent Zoo
=========

We have provided a number of pre-trained agents in the `agent_zoo` directory.

To see a humanoid run towards a random varying target:

```bash
python agent_zoo/RoboschoolHumanoidFlagrun_v0_2017may.py
```

To see three agents in a race:

```bash
python agent_zoo/demo_race2.py
```

** Development guide

git subtree add --prefix jsbsim https://github.com/JSBSim-Team/jsbsim.git master --squash 
