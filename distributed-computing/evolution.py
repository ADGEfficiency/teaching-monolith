import os
from os.path import join

import gym
import numpy as np


def forward_mountaincar(x, params):
    #  sometimes gym gives (2, 1) from mountaincar
    x = np.array(x).reshape(-1)
    #  input -> hidden
    z0 = x.dot(params['w0']) + params['b0']
    #  relu
    a0 = np.maximum(z0, 0)
    #  hidden -> output
    return a0.dot(params['w1']) + params['b1']


def forward_cartpole(x, params, threshold=0.5):
    x = np.array(x).reshape(-1)
    #  input -> hidden
    z0 = x.dot(params['w0']) + params['b0']
    #  relu
    a0 = np.maximum(z0, 0)
    #  hidden -> output
    z1 = a0.dot(params['w1']) + params['b1']
    #  sigmoid
    a1 = 1 / (1 + np.exp(-z1))
    return np.where(a1 > threshold, 1, 0)[0][0]


def make_env(env_id='CartPole-v0'):
    env = gym.make(env_id)
    if env_id == 'CartPole-v0':
        return env, forward_cartpole, env.observation_space.shape[0], 1
    elif env_id == 'MountainCarContinuous-v0':
        return env, forward_mountaincar, env.observation_space.shape[0], env.action_space.shape[0]
    else:
        raise ValueError('env {} not supported'.format(env_id))


def initialize_parameters(i_size, h_size, o_size):
    return {
        'w0': np.random.randn(i_size, h_size),
        'b0': np.zeros((1, h_size)),
        'w1': np.random.randn(h_size, o_size),
        'b1': np.zeros((1, o_size))
    }


def episode(params, render=False, env_id='MountainCarContinuous-v0'):
    env, forward, _, _ = make_env(env_id)
    done = False
    rewards = []
    obs = env.reset()
    while not done:
        action = forward(obs, params)
        next_obs, reward, done, info = env.step(action)
        rewards.append(reward)
        obs = next_obs
        if render:
            img = env.render(mode='human')
    return sum(rewards)


def save_params(params, env_id, agent_id=0):
    home = join('agents', env_id, 'agent_{}'.format(agent_id))
    os.makedirs(home, exist_ok=True)
    print('saving to {}'.format(home))
    for k, arr in params.items():
        np.save(join(home, '{}.npy'.format(k)), arr)


def load_params(env_id, agent_id):
    home = join('agents', env_id, 'agent_{}'.format(agent_id))
    print('loading from {}'.format(home))
    params = [join(home, p) for p in os.listdir(home) if 'npy' in p]
    return {
        p.split('/')[-1].split('.')[0]: np.load(p) for p in params
    }
