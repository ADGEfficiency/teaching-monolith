# Distributed Computing

A one day course on distributed computation in Python:

- functional programming,
- threads, `multiprocessing` and `asyncio`,
- Python ecosystem,
- MapReduce, Spark, `ray` & `dask`.

Outcomes:

- an introduction to the ecosystem of distributed computing with Python,
- how to program in a functional style,
- why `multiprocessing` is a data scientist's best friend,
- differences between using threads / processes in Python,
- difference between concurrency and parallelism.

Practical work:

- [functional-programming.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/distributed-computing/functional-programming.ipynb) - [run with binder](https://mybinder.org/v2/gh/ADGEfficiency/teaching-monolith/HEAD?labpath=distributed-computing%2Ffunctional-programming.ipynb),
- [multiprocessing.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/distributed-computing/functional-programming.ipynb) - [run with binder](https://mybinder.org/v2/gh/ADGEfficiency/teaching-monolith/HEAD?labpath=distributed-computing%2Fmultiprocessing.ipynb),
- mapreduce,
- asyncio.


## Ecosystem Cheat Sheet

| Framework         | Compute | Language | Number of machines | Problem |
| ---               | ---     | ---      | ---                | --- |
| `threading`         | CPU     | Python   | One                | IO |
| `multiprocessing` | CPU     | Python   | One                | CPU |
| `dask`            | CPU     | Python   | Many               | IO + CPU |
| `ray`             | CPU     | Python   | Many               | IO + CPU |
| Rapids            | GPU     | Python   |  Probably multi-GPU    | |
| Hadoop MapReduce  | CPU     | Java     | Many               | CPU |
| Spark             | CPU     | Java (Scala)     | Many               | CPU |


## Single machine options in Python

Multiple threads with `threading`:

- IO bound problems,
- global interpreter lock (GIL) prevents parallel compute with threads (in Python),
- threading (in Python) is not useful for CPU bound tasks (you can only run one thread at once).

Multiple processes with `multiprocessing`:

- CPU bound problems,
- requires memory than threads,
- good solution for many data science problems - often we are CPU bound.

Asynchronous with `asyncio`:

- IO bound problems,
- able to do concurrent computation in a single thread.


## Multiple machines in Python

- `dask`,
- `ray`,
- `pyspark` (Python binding for Spark).


## Batch processing

<img src="assets/f1.png" width="400" height="400">

*Designing Data-Intensive Applications - The Big Ideas Behind Reliable, Scalable, and Maintainable Systems - Martin Kleppmann*


## Functional programming

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ADGEfficiency/teaching-monolith/HEAD?labpath=distributed-computing%2Ffunctional-programming.ipynb)

Functional programming concepts (such as map, filter, and reduce) are the atomic operations of many distributed computing frameworks.

One example is mapping over a pool of processes:

```python
from multiprocessing import Pool

with Pool(popsize, maxtasksperchild=32) as pool:
    results = p.starmap(episode, zip(population, seeds))
```

## Foundational Examples

<img src="assets/examples.png" width="768" height="768">

Lawn mowing - can be split into independent tasks (different patches of the lawn).

Baby making - cannot be sped up.

A chess grandmaster playing many games of chess against amateurs at once:

- grandmaster takes 5 minutes to make a move,
- amateurs take 1 hour,
- games can be played quicker if the grandmaster moves to the next board while the amateur is thinking,
- grandmaster never acts in parallel (only one game at a time), but does act concurrently.

## Concurrency

[Wikipedia](https://en.wikipedia.org/wiki/Concurrency_(computer_science))

Concurrency = **dealing with many things** at once - it is the **structure** of a program - whether we can execute a program in a different order.
 
For a concurrent program, the order doesn't matter:

- can be run in a different order sequentially,
- can be run in parallel,
- tasks can overlap.

Concurrency requires communication and coordination (often waiting) - it can be used to make use of limited hardware (like a single thread).  

In IO bound problems we mostly wait (reading/writing to disk, using the network) - in a concurrent program, this waiting time can be used to do other things (and thereby deal with many things at once).


## Parallelism

Parallelism = **doing many things** at once - it is how we can **execute** of a program.  Parallelism is a special case of concurrency.

A key characteristic of a parallelizable task is **independence** - we need to be able to split the work into many tasks that can run independently - this naturally favours a functional style of programming (where our functions have no side effects and we don't rely or are affected by state).

We could parallelize across:

- threads (in one CPU core),
- CPU cores (in one machine),
- multiple machines,
- multiple data centres,
- multiple regions,
- multiple planets.

Key oppourtunities for parallelism in code = `for` loops, `maps`.


## Things we do with computers

1. Compute - transform data,
2. Memory - store data,
3. Network - send/receive data.


## The problems we can have with computers

1. Compute - doing lots of compute - CPU bound,
2. Memory - not enough storage (RAM or disk) - out of memory (OOM),
3. Network - waiting to read/write data (network, disk) = IO bound.


## How can we make computer program go faster?

CPU bound problem:

- doing the sequential computation faster (faster processor),
- doing the computation in parallel faster (more processors).

Memory problem:

- processing data in smaller chunks,
- more memory.

IO bound problem:

- doing something else while we are waiting.

Data scientists will mostly be concerned with CPU bound problems - but memory tends to be the limiting factor (RAM is expensive, and has historically been the limit on computers, not processor speed).  

GPUs are an excellent example of this.


## How do computers compute

CPU core:

- hardware,
- runs one sequence of computation at a time,
- fundamentally sequential,
- speed measured in cycles per second (GHz).

Threads:

- software,
- sequence of computation,
- shared memory between threads.

Process:

- software,
- program that runs threads,
- dedicated memory space.


## How can we do compute faster?

Two options:

- faster processor (more cycles per second, GHz),
- do compute in parallel.

Diminishing returns on increasing processor speeds:

- Moore's Law (processor speeds doubling every two years) is coming to an end

Trend in modern computing is more processors:

- more CPU cores (common to have 8-16 on laptops),
- GPU is this in the extreme (thousands of CPU cores).

These cores can be on the same machine:

- also be on many different machines,
- many machines = **distributed computation**.

The cloud is made up of many small machines working together:

- cheaper to run lots of small machines than less, larger machines,
- a key challenge is dealing with machine failure (fault tolerance).


## Should I use multiple machines?

- what is your problem (CPU bound or IO bound),
- what language are you working in,
- who is paying,
- is it a one off or a repeated computation.

Distributed computing is fundamentally harder:

- fixed & variable overhead of communication & coordination,
- machine failure.


## Cheat sheet (Python specific)

CPU bound problems:

- parallelize across cores,
- parallelize with GPU.

IO bound problem:

- threading,
- async.

Memory problems:

- being careful about `dtypes` (0 or 1 versus `'true'` and `'false'`),
- only read in columns you need,
- process data in chunks (row wise),
- bigger machine.

GPU memory problems:

- reduce model size,
- reduce batch size,
- get a bigger GPU.

Question - what are the drawbacks with these three?


## Single machine options in Python

Multiple threads:

- `threading`,
- IO bound problems,
- GIL prevents parallel compute with threads -> not useful for CPU bound tasks.

Multiple processes:

- `multiprocessing`,
- CPU bound problems,
- more memory than threads,
- good solution for data science.

Asynchronous:

- `asyncio`,
- IO bound problems,
- concurrent computation in a single thread.


## Multiple machines in Python

- `dask`
- `ray`
- `pyspark` (Python binding for Spark)


## Don't forget about Bash

From *Designing Data-Intensive Applications - The Big Ideas Behind Reliable, Scalable, and Maintainable Systems - Martin Kleppmann*
- we can process gigabytes of data in seconds with our friendly, always available bash tools:

```bash
cat ~/.bash_history | 
  awk '{print $0}' |  #  not needed!
	sort |  # `sort` = repeated commands n times in a row
	uniq -c | # `uniq` = filers out repeats with a counter
	sort -r -n | # `sort` = by count, in reverse order
	head -n 10
```

Lots can be done with compositions of classics like `sed`, `grep`, `sort`, `uniq`, `xargs` - `sort` and `xargs` will both parallelize across CPU cores.


## Python standard library concurrent computation options

|                   | Threads     | Processes         | Async       |
|-------------------|-------------|-------------------|-------------|
| Library           | `threading` | `multiprocessing` | `aysncio`   |
| Use all CPU cores | no          | yes               | no          |
| Scalability       | 100's       | 10's              | 1000's      |
| GIL problems      | yes         | no                | no          |
| Use case          | IO bound    | CPU bound         | IO bound    |
| Uses OS scheduler | yes         | yes               | no          |
| Multitasking      | preepmtive  | preepmtive        | cooperative |


## Sharing isn't always a good thing

Sharing data can be a problem - [race conditions](https://en.wikipedia.org/wiki/Race_condition).

Solution = place [locks](https://en.wikipedia.org/wiki/Lock_(computer_science)) at critical points in multithreaded code:
- a lock (aka mutex - mutual exclusion) enforces limits on access to resources - commonly memory,
- locks add overhead.

This can cause more problems - [resource starvation](https://en.wikipedia.org/wiki/Starvation_(computer_science)) = denial of access to required resources - [deadlocks](https://en.wikipedia.org/wiki/Deadlock) = threads waiting on threads waiting on threads.

Sharing memory is hard - writing multithreaded code in Python is hard - [Raymond Hettinger, Keynote on Concurrency, PyBay 2017](https://www.youtube.com/watch?v=9zinZmE3Ogk) for a detailed example of how to write multithreaded code properly in Python.


## Thread safety

Thread safety = avoiding race conditions that can occur with shared memory - often done using locks.


## `threading`

**Python is not thread safe**.

Python's Global Interpreter Lock (GIL) provides memory safety in Python, at the cost of limiting Python threads to a single core
- the GIL locks onto a a single core.

Threads share memory - they exist in the same process, and same memory space.  It's possible that one thread mutates data needed by another thread.  This makes threads lightweight (in terms of memory) but unsafe (in Python).

`threading` will allow concurrent computation on one thread at a time on a single core:

- not parallelism,
- threads will take turns executing tasks,
- suitable for IO bound problems.

Difficult to get right - if you have an IO bound problem, `asyncio` is a safer choice than attempting multi-threading in Python.

[Raymond Hettinger, Keynote on Concurrency, PyBay 2017](https://www.youtube.com/watch?v=9zinZmE3Ogk) is a good talk on this topic.


## `multiprocessing`

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ADGEfficiency/teaching-monolith/HEAD?labpath=distributed-computing%2Fmultiprocessing.ipynb)

Processes do not share memory - they exist in their own same memory space.  This makes using many processes in parallel expensive in terms of memory, but much safer.

Communication between Python processes is possible (via pickling) - but you probably don't want to do this (tasks should be independent) - communication = dependency.

No sharing of memory means the GIL isn't a problem - this makes `multiprocessing` our tool of choice for single machine parallel computation.

Means we can parallelize across cores! We can use all the hardware we have, in Python (no more single core)!


## MapReduce

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ADGEfficiency/teaching-monolith/HEAD?labpath=distributed-computing%2Fmapreduce.ipynb)

[Wikipedia](https://en.wikipedia.org/wiki/MapReduce)

Implementation independent - a method of processing data across multiple machines.

Developed by Google - fundamental to scaling on commodity hardware - now replaced by many other things.

MapReduce is a system for orchestrating distributed & parallel computation:

- execution engine that manages communication & data transfer,
- parallelism provides scalability, redundancy & fault tolerance,
- data = Google File System (GFS),
- compute = MapReduce.

An example of *split-apply-combine*:

1. map = splits input into n tasks,
2. shuffle = workers redistribute data based on map results, so all members of each key are on the same worker node,
3. reduce = process data per key.


## Why can MapReduce be parallel

Map is independent and reduce is independent.  The reduce works on data that all has the same key - the order of combining doesn't matter (concurrent).

[mapreduce.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/distributed-computing/mapreduce.ipynb)



## Apache Hadoop

https://en.wikipedia.org/wiki/Apache_Hadoop

https://github.com/andkret/Cookbook/blob/master/sections/03-AdvancedSkills.md#hadoop-platforms

Hadoop is open source 
- includes an implementation of MapReduce
- data = Hadoop Distributed File System (HDFS)
- writes intermediate data to disk


## Apache Spark

https://en.wikipedia.org/wiki/Apache_Spark

https://github.com/andkret/Cookbook/blob/master/sections/03-AdvancedSkills.md#apache-spark

More complex data transformations than MapReduce:

- keeps intermediate data in memory.

Spark:

- runs in a JVM (Java) - many businesses run on Java and have access to a JVM,
- written in Scala - has Java & Python bindings,
- more mature, more features.

Extension of Hadoop MapReduce:

- ML, SQL, streaming, graph processing.

Use for parallel data processing - query optimizer.

Tabular data / dataframe based.

Has Python bindings `pyspark`.


## Dask

[Detailed introduction to Dask](https://docs.dask.org/en/latest/)

[Comparison to Spark](https://docs.dask.org/en/latest/spark.html)

Dask
- Python
- has a generic task scheduler
- **use for dataframe type operations**

Dask offers the ability to
- process larger than memory datasets
- parallelize compute

Couples with pandas, numpy
- not entire reimpelemtations


### Dask Tutorial

We will work through a few sections of the [dask tutorial](https://tutorial.dask.org/00_overview.html).

We will look at:

- 01_dask.delayed.ipynb - lazy compute
- 03_array.ipynb - data larger than memory
- 04_dataframe.ipynb
- 05_distributed.ipynb


### Dask delayed best practices

[Best practices](https://docs.dask.org/en/latest/delayed-best-practices.html)

Call delayed on the function, not the result

```python
#  lazy - do this
dask.delayed(f)(x, y)

# immediate - don't do this!
dask.delayed(f(x, y))
```

Include lot's of `dask.delayed` in each `dask.compute` call - ideally want one compute call on a large graph.


## ray

[docs](https://ray.readthedocs.io/en/latest/) - [github](https://github.com/ray-project/ray) - [tutorials](https://github.com/ray-project/tutorial)

```bash
pip install 'ray[all]'

python ray_example.py
```

- task scheduler (same as Dask)
- allows shared state between tasks (`Actor` model)
- bottom up scheduling

Turn off your VPN!
- get problems wint connecting to the redis database

https://github.com/ray-project/ray/issues/642

> Ray uses a distributed bottom-up scheduling scheme in which workers submit tasks to local schedulers, and local schedulers assign tasks to workers. Local schedulers can also forward tasks to global schedulers which can load balance between machines. Dask uses a centralized scheduler, which manages all tasks for the cluster. The point of the bottom-up scheduling approach is to improve task latency and throughput.

Distributed:
- hyperparameter tuning [guide](https://ray.readthedocs.io/en/latest/tune-usage.html)
- reinforcement learning
- model training


### ray tune

Hyperparameter tuning library in ray 
- can be used with keras, sklearn, pytorch

Tutorials:
- basics - [colab](https://colab.research.google.com/github/ray-project/tutorial/blob/master/tune_exercises/exercise_1_basics.ipynb) - [github](https://github.com/ray-project/tutorial/blob/master/tune_exercises/exercise_1_basics.ipynb)


## Asynchrony

[Wikipedia](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming))

How to deal with events outside the main flow of the program

We want to not block the main program while we are waiting for outside events

This provides a degree of parallelism

Common to use a future/promise - subroutines return these to represent the ongoing event.


## Async IO

Async IO = programming paradigm (language independent)
- equivalent to threads or processes
- `asyncio` is the Python implementation
- single thread, single core

Offers concurrency (not parallelism)
- way to do deal with many things at once with a single thread!

Require two things
- asyncronous functions, that can stop & start
- event scheduler

async / await = API for asynchronous programming

Uses
- IO bound, networking
- IO from a socket is ready for reading / writing
- GUI

Speed will be limited by the slowest step
- https://en.wikipedia.org/wiki/Amdahl%27s_law
- https://en.wikipedia.org/wiki/Rate-determining_step


### Coroutine

[Wikipedia](https://en.wikipedia.org/wiki/Coroutine)

Function that can pause to let others run
- specalized Python generator

Async routines can pause (to let other routines run)
- can stop it's execution before returning
- can pass control to another coroutine


### Cooperative multitasking

Key difference in async versus threads

Threads don't decide when to run - they can switch anytime
- preemptive multitasking 
- OS decides when to run (as for all other programs on your machine)

This can be a problem when things need to be done in a certain order
- this is solved by putting locks in critical sections in multithreaded code

Async switches co-operatively
- cooperative multitasking
- coroutines decide when to run/not run (defined in code)
- control when task switching occurs
- explicitly add `yield` or `await` to cause task switching


## Event loop

[Wikipedia](https://en.wikipedia.org/wiki/Event_loop)

Knows about all the tasks
- when function suspends, control returned to the loop, which then finds another function

Loop that waits & dispatches events
- makes requests of event providers
- calls relevant event handlers

Watches for something to happen, then calls code that cares about what happened

Often the highest level of control in a program
- event A happens (button clicked)
- event A sent to event loop
- event loop checks for a callback registered to handle that click
- callbacks are called, using info from the click

`asyncio` provides an event loop


## `asyncio`

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ADGEfficiency/teaching-monolith/HEAD?labpath=distributed-computing%2Fasyncio.ipynb)

Cheap task switches
- calling Python function has more overhead than restarting a generator or an awaitable
- functions need to build a new stack frame on each call - generator already has the stack frame built
- async is cheap

The cost of using async is that you need to use non-blocking versions of many things you do alot
- `file.read()`
- `time.sleep()`

The cost of async is the learning curve
- event loop, all calls non-blocking, async + await
- lots of code, lots knowledge


## `async` / `await`

`asyncio` = Python package for managing coroutines

`async` / `await` = Python keywords used to define coroutines

Need to use async versions of many blocking functions from stlib


## Resources / References

[Parallel Programming with numpy and scipy](https://scipy-cookbook.readthedocs.io/items/ParallelProgramming.html)

[Raymond Hettinger, Keynote on Concurrency, PyBay 2017](https://www.youtube.com/watch?v=9zinZmE3Ogk)

[Itamar Turner-Trauring: Small Big Data: using NumPy and Pandas when your data... | PyData NYC 2019](https://www.youtube.com/watch?v=uya_MHnoKa0)

[Tom Augspurger: Scalable Machine Learning with Dask | PyData New York 2019](https://www.youtube.com/watch?v=we1m4-IsbL8)

Designing Data-Intensive Applications - The Big Ideas Behind Reliable, Scalable, and Maintainable Systems - Martin Kleppmann 

[Challenges with distributed systems - Amazon](https://aws.amazon.com/builders-library/challenges-with-distributed-systems/)

[Eric Dill: Is Spark still relevant? Multi-node CPU and single-node GPU workloads.. | PyData NYC 2019](https://www.youtube.com/watch?v=obKZzFRNTxo)

[Learning Spark: Lightning-Fast Big Data Analysis - Patrick Wendell & Matei Zaharia](http://shop.oreilly.com/product/0636920028512.do)

[Multiprocessing Vs. Threading In Python: What You Need To Know](https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/)

[Async IO in Python: A Complete Walkthrough - Real Python](https://realpython.com/async-io-python/)
