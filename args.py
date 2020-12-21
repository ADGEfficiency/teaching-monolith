import argparse

# click

parser = argparse.ArgumentParser()
parser.add_argument('--start_index')
args = parser.parse_args()

print(args.start_index)

