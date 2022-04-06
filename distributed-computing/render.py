import argparse

from evolution import episode, load_params


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--env_id", default="CartPole-v0", nargs="?")
    parser.add_argument("--agent_id", default=8, nargs="?")
    args = parser.parse_args()
    params = load_params(args.env_id, args.agent_id)
    reward = episode(params, env_id=args.env_id, render=True)
    print("total episode reward {}".format(reward))
