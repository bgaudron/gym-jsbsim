import os

from gym.envs.registration import registry, register, make, spec
from gym_jsbsim.envs.heading_control_task import HeadingControlTask

"""
This script registers JSBSimEnv

with OpenAI Gym so that they can be instantiated with a gym.make(id,task,aircraft_name)

 command.

 To use do:

       env = gym.make('GymJsbsim-{task}-{aircraft_name}-v0')
"""

import gym_jsbsim

tasks = dict(HeadingControlTask=HeadingControlTask)

#for aircraft_name in aircraft_names:
for task in tasks:
    register(
        id=f'GymJsbsim-{task}-v0',
        entry_point='gym_jsbsim.jsbsim_env:JSBSimEnv',
        kwargs=dict(task=tasks[task])
    )
