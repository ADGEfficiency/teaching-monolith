import ray
import time


@ray.remote
def f(x):
    print('hi from {}'.format(x))
    return x

# Start Ray.
ray.init()

# Start 4 tasks in parallel.
result_ids = []
for i in range(4):
    result_ids.append(f.remote(i))

# Wait for the tasks to complete and retrieve the results.
# With at least 4 cores, this will take 1 second.
results = ray.get(result_ids)  # [0, 1, 2, 3]
