import argparse

from evolution import episode, load_params


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent_id', default=8, nargs='?')
    args = parser.parse_args()
    params = load_params(args.agent_id)
    reward = episode(params, render=True)
    print('total epsisode reward {}'.format(reward))
    