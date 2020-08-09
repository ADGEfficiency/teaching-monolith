# Distributed Computing

A one day course on distributed computation in Python, covering:
- functional programming
- `multiprocessing`, threads, `asyncio`
- MapReduce, Spark
- `ray`, `dask`

Key outcomes
- how to program in a functional style
- why `multiprocessing` is a data scientists best friend
- ecosystem of multimachine computation with Python

Additional outcomes (not exhaustive)
- differences between using threads / processes in Python
- difference between concurrency and parallelism


## Ecosystem

| Framework         | Compute | Language | Number of machines |
| ---               | ---     | ---      | ---                |
| `threads`         | CPU     | Python   | One                |
| `multiprocessing` | CPU     | Python   | One                |
| `dask`            | CPU     | Python   | Many               |
| `ray`             | CPU     | Python   | Many               |
| Rapids            | GPU     | Python   | ?                  |
| Hadoop MapReduce  | CPU     | Java     | Many               |
| Spark             | CPU     | Java     | Many               |


## Resources

[Raymond Hettinger, Keynote on Concurrency, PyBay 2017](https://www.youtube.com/watch?v=9zinZmE3Ogk)

[Itamar Turner-Trauring: Small Big Data: using NumPy and Pandas when your data... | PyData NYC 2019](https://www.youtube.com/watch?v=uya_MHnoKa0)

[Tom Augspurger: Scalable Machine Learning with Dask | PyData New York 2019](https://www.youtube.com/watch?v=we1m4-IsbL8)

Designing Data-Intensive Applications - The Big Ideas Behind Reliable, Scalable, and Maintainable Systems - Martin Kleppmann 
[Challenges with distributed systems - Amazon](https://aws.amazon.com/builders-library/challenges-with-distributed-systems/)

[Eric Dill: Is Spark still relevant? Multi-node CPU and single-node GPU workloads.. | PyData NYC 2019](https://www.youtube.com/watch?v=obKZzFRNTxo)

[Learning Spark: Lightning-Fast Big Data Analysis - Patrick Wendell & Matei Zaharia](http://shop.oreilly.com/product/0636920028512.do)

[Multiprocessing Vs. Threading In Python: What You Need To Know](https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/)

[Async IO in Python: A Complete Walkthrough - Real Python](https://realpython.com/async-io-python/)


## Batch processing

![](assets/f1.png)
*from Designing Data-Intensive Applications - The Big Ideas Behind Reliable, Scalable, and Maintainable Systems - Martin Kleppmann*


## Functional programming

Concepts from functional programming (map, filter, reduce) are crucial to understand many of the tools we will look at today.

We will go over these concepts in [functional-programming.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/distributed-computing/functional-programming.ipynb).


## Concurrency and parallelism

[Concurrency - Wikipedia](https://en.wikipedia.org/wiki/Concurrency_(computer_science))

Concurrency = dealing with lots of things at the same time
- **structure** of a program
- ability to execute parts in a different order

Parallelism = doing many things at the same time
- **execution** of a program
- special case of concurrency

*Draw example on whiteboard*


## Concurrency

Concurrent = the order doesn't matter
- can be run in a different order sequentially
- can be run in parallel
- tasks that can overlap

Example of a chess grandmaster playing 24 amateurs at once
- grandmaster takes 5 minutes to make a move
- amateurs take 1 hour
- games can be played quicker if the grandmaster moves to the next board while the amateur is thinking

Requires communication and coordination

Concurrency can be useful with limited hardware
- when we are doing IO, we often need to wait for the device (reading/writing to disk)
- if we have a concurrent program, this time can be used to run other threads


## Parallelism

Doing many things at the same time
- how we execute a program

What can be made parallel
- key requirement is independence
- lawn mowing versus baby making 

Parallel across
- CPU cores (single machine)
- multiple machines
- multiple data centres
- multiple regions


## Three systems for processing/delivering data

Batch processing (this course)
- offline
- once per day/hour style updates

Streaming
- real time
- inbetween online & offline
- kafka, kubernetes
 
Services
- online, want immediate reply
- websites, REST API, databases


## Two things we do with computers

Compute 
- transforming data

Memory 
- storing data


## What do we want from computers

Do many things at the same time
- doing lots of compute quickly
- handling many requests (web server) at once

Do things fast
- this is a special case of doing many things at once


## What slows down computer programs?

What problems do we have
- CPU bound
- IO bound
- memory problem

Doing lots of computation
- CPU bound

Waiting to read/write data (network, disk)
- IO bound

Not enough storage (RAM or disk) for data
- memory problem


## How can we make computer programs faster?

CPU bound problem
- doing the sequential computation faster (faster processor)
- doing the computation in parallel faster (more processors)

IO bound problem
- doing something else while we are waiting

Memory problem
- processing data in smaller chunks
- more memory

Data scientists will mostly be concerned with CPU bound problems


## How do computers compute

CPU core
- hardware
- runs one sequence of computation at a time
- fundamentally sequential
- speed measured in cycles per second (GHz)

Threads
- software
- sequence of computation
- shared memory between threads

Process
- software
- program that runs threads
- dedicated memory space


## How can we do compute faster?

Two options
- faster processor (more cycles per second, GHz)
- do it in parallel

Diminishing returns on increasing processor speeds
- Moore's Law (processor speeds doubling every two years) is coming to an end

Trend in modern computing is more processors
- more CPU cores (common to have 8-16 on laptops)
- GPU this in the extreme (thousands of CPU cores)

These cores can be on the same machine
- also be on many different machines
- many machines = distributed computation

The cloud is made up of many small machines working together
- cheaper to run lots of small machines than less, larger machines
- a key challenge is dealing with machine failure (fault tolerance)


## Should I use multiple machines?

- what is your problem (CPU bound or IO bound)
- what language are you working in
- who is paying
- is it a one off or a repeated computation

Distributed computing is fundamentally harder
- fixed & variable overhead of communication & coordination
- machine failure


## Cheat sheet (Python specific)

CPU bound problem
- parallelize across cores
- parallelize with GPU

IO bound problem
- threading
- async

Memory problems (RAM)
- being careful about `dtypes` (0 or 1 versus `'true'` and `'false'`)
- only read in columns we need
- process data in chunks
- bigger machine

GPU memory problems
- reduce model size
- reduce batch size
- get a bigger GPU

Question - what are the drawbacks with these three?


## Single machine options in Python

Multiple threads
- `threading`
- IO bound problems
- GIL prevents parallel compute with threads -> not useful for CPU bound tasks

Multiple processes
- `multiprocessing`
- CPU bound problems
- good solution for data science!

Asynchronous
- `asyncio`
- IO bound problems
- concurrent computation in a single thread


## Multiple machines in Python

- `dask`
- `ray`
- `pyspark` (Python binding for Spark)


## Don't forget about Bash

Cool example from Designing Data-Intensive Applications 
- can process gigabytes of data in seconds

```bash
cat ~/.bash_history | 
  awk '{print $0}' |  #  not needed!
	sort |  # `sort` = repeated commands n times in a row
	uniq -c | # `uniq` = filers out repeats with a counter
	sort -r -n | # `sort` = by count, in reverse order
	head -n 10
```

Lots can be done with clever combinations of `sed`, `grep`, `sort`, `uniq`, `xargs`
- `sort` will parallelize across CPU cores


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

Sharing data can be a problem
- [race conditions](https://en.wikipedia.org/wiki/Race_condition)

Solution = place [locks](https://en.wikipedia.org/wiki/Lock_(computer_science)) at critical points in multithreaded code 
- a lock (aka mutex - mutual exclusion) enforces limits on access to resources - commonly memory
- locks add overhead

This can cause more problems
- [resource starvation](https://en.wikipedia.org/wiki/Starvation_(computer_science)) = denial of access to required resources
- [deadlock](https://en.wikipedia.org/wiki/Deadlock) = threads waiting on threads waiting on threads

Conclusion = sharing memory is hard!
- writing good multithreaded code is hard
- [Raymond Hettinger, Keynote on Concurrency, PyBay 2017](https://www.youtube.com/watch?v=9zinZmE3Ogk) for a detailed example of how to write multithreaded code properly


## `threading`

Python is not thread safe
- safety = avoiding race conditions that can occur with shared memory
- done using locks

Python's Global Interpreter Lock (GIL) provides safety
- at the cost of limiting Python threads to a single core
- locked onto a single core

`threading` allows concurrent computation on a single core
- not parallelism
- threads take turns executing tasks
- better for IO - IO often means waiting for the network/disk

Difficult to get right


## `multiprocessing`

Processes = no sharing
- requires object pickling for communication

No sharing of memory means the GIL isn't a problem
- tool for parallel computation

Means we can parallelize across cores!
- we can use all the hardware we have, in Python!

Python has the `multiprocessing` library for doing parallel computation on a single machine
- only way for multicore concurrency in Python

We will take a look at it in [multiprocessing.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/distributed-computing/multiprocessing.ipynb).


## MapReduce

https://en.wikipedia.org/wiki/MapReduce

Implementation independent
- way to process data across multiple machines

Developed by Google - fundamental to them scaling on commodity hardware
- now replaced by streaming systems (MapReduce is batch data processing)

System for orchestrating distributed & parallel computation
- execution engine that manages communication & data transfer
- parallelism provides scalability, redundancy & fault tolerance

- data = Google File System (GFS)
- compute = MapReduce

Split-apply-combine

1. map
2. shuffle = workers redistribute data based on map results, so all members of each key are on the same worker node
3. reduce = process data per key


## Why can MapReduce be parallel

Map is independent

Reducer 
- works on data that all has the same key or
- order of combining doesn't matter 

[mapreduce.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/distributed-computing/mapreduce.ipynb)


## Multiple machine computation in Python

- Hadoop
- Spark
- dask
- ray


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

More complex data transformations than MapReduce
- keeps intermediate data in memory

Spark
- runs in a JVM (Java) - many businesses run on Java and have access to a JVM
- written in Scala - has Java & Python bindings
- more mature, more features

Extension of Hadoop MapReduce
- ML, SQL, streaming, graph processing

Use for parallel data processing
- query optimizer

Tabular data / dataframe based

Has Python bindings `pyspark`


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

We will work through a few sections of the Dask tutorial
- [dask/dask-tutorial](https://github.com/dask/dask-tutorial)

We will look at:
- 01_dask.delayed.ipynb - lazy compute
- 03_array.ipynb - data larger than memory
- 04_dataframe.ipynb
- 05_distributed.ipynb
- 
```
$ git clone http://github.com/dask/dask-tutorial
```

You can build a docker image out of the provided Dockerfile.

```bash
$ docker build . # This will build using the same env as in a)
```

Run a container, replacing the ID with the output of the previous command

```bash
$ docker run -it -p 8888:8888 -p 8787:8787 <container_id_or_tag>
The above command will give an URL (Like http://(container_id or 127.0.0.1):8888/?token=<sometoken>) which can be used to access the notebook from browser. You may need to replace the given hostname with "localhost" or "127.0.0.1".
```

Need the below to get visualize to work:

```bash
!conda install -c conda-forge graphviz -y
!conda install -c conda-forge python-graphviz -y
```

Also need to move some of the `%%time` lines into the cell below


### dask delayed best practices

[Best practices](https://docs.dask.org/en/latest/delayed-best-practices.html)

Call delayed on the function, not the result

```python
#  lazy - do this
dask.delayed(f)(x, y)

# immediate - don't do this!
dask.delayed(f(x, y))
```

Include lot's of `dask.delayed` in each `dask.compute` call
- ideally want one compute call on a large graph


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

https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)

How to deal with events outside the main flow of the program

We want to not block the main program while we are waiting for outside events

This provides a degree of parallelism

Common to use a future/promise
- subroutines return these to represent the ongoing event


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

https://en.wikipedia.org/wiki/Coroutine

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

https://en.wikipedia.org/wiki/Event_loop

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


## Example

[asyncio.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/distributed-computing/asyncio.ipynb)
