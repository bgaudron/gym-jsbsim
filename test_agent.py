import gym
import gym_jsbsim
import numpy as np
import sys

def relu(x):
    return np.maximum(x, 0)

class RandomPolicy():
    "Simple random policy, no internal state"
    dim = 0

    def __init__(self, ob_space, ac_space):
        assert ac_space.shape[0] != 0
        self.dim = ac_shape.dim[0]

    def act(self, ob):
        x = np.random.rand(self.dim) # Create random action vector
        return x

def demo_run(episodes=100):
    env = gym.make("GymJsbsim-HeadingControlTask-v0") # Can we have aircraft type as an additional parameter
    env.unwrapped.configure(sys.argv[1])
    env.reset()

    pi = RandomPolicy(env.observation_space, env.action_space)

    while 1:
        frame = 0
        score = 0
        obs = env.reset()

        while 1:
            a = pi.act(obs)
            obs, r, done, _ = env.step(a)
            score += r
            frame += 1

            if not done: 
                continue

            print("score=%0.2f in %i frames" % (score, frame))

if __name__ == "__main__":
    demo_run()
