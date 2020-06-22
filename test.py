import gym
import tensorflow as tf 

def MDP():
    pass

def main():
    env = gym.make('CartPole-v0')
    env.reset()
    for _ in range(100):
        env.render()
        env.step(env.action_space.sample()) # take a random action
    env.close()

if __name__ == "__main__":
    main()