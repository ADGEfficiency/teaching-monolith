## TODO

- use binary constraints somewhere?


## Resources & Further Reading

- [a linear program to dispatch electric battery storage](https://github.com/ADGEfficiency/energy-py-linear)

my blog post on forecast quality in energypy linear


- [6 part blog post series on linear programming with PuLP - Ben Alex Keen](http://benalexkeen.com/blog/)
- [Linear programming - Michel Goemans](https://math.mit.edu/~goemans/18310S15/lpnotes310.pdf)
- [Linear programming - Thomas Ferguson](https://www.math.ucla.edu/~tom/LP.pdf)

[Linear programming - Wikipedia](https://en.wikipedia.org/wiki/Linear_programming)


# Linear Programming

A two hour course on linear programming - a useful optimization technique.

Key outcomes:

- what is linearity & why is it important to optimization,
- three components of a linear program,
- things that make a program non-linear,
- the value of linearity to linear programming.

Practical work in [linear-programming.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/linear-programming/linear-programming.ipynb).


## Using linear programs to solve business problems

Writing linear programs requires two skills:

1. identifying the business problem can be modelled as a linear program,
2. writing the objective, variables and constraints of that program.

The first step is harder!

You don't need to write the solver, or understand how a linear programming solver works.

You can be an effective driver without understanding the chemistry of combustion - you can also solve business problems without understanding the math behind linear programming.


## What is linear programming?

A constrained optimization method:

- minimize cost or maximize profit,
- under some constraints,
- by changing some variables.

The important feature of linear programming that distinguishes it from other optimization methods:

- guaranteed to find the global optimum - will run deterministically, with no reliance on initial conditions.

Other optimization methods are either non-linear and/or unconstrained:

- non-linear programming - constrained, non-linear,
- stochastic gradient descent - unconstrained, non-linear,
- evolutionary optimization - unconstrained, non-linear.

Training neural networks:

- loss = highly non-linear,
- unconstrained = weights can take on any values,
- very sensitive to weight initialization.

Important to note that for deep learning, we never find the global optimum for any neural network loss surface - but local optima are 'good enough'.


## Why not linear programming?

Many problems are not linear - the cost surface (objective function) of a neural network loss

- but if yours is, linear programs are a huge advantage.

Linear programs don't offer any estimate of uncertantity - see [robust optimization](https://en.wikipedia.org/wiki/Robust_optimization).


## Three components of a linear program

1. **Objective function** - minimize or maximize,
2. **Variables** - things you can change - continuous, integer or binary,
3. **Constraints** - equality `==` or inequality `>=`, `<=`.


### 1. Objective function

Also called a cost function (loss in deep learning).

Represents what you want to do - can be either maximization or minimization.


### 2. Variables

Variables can be contionuous, integer or binary - binary variables are often used as on/off variables.

A *mixed integer linear program* (MILP) is a linear program where some of the variables are integer - will require an MILP solver.

Most LP is MILP - integer & binary variables are useful to writing linear programs.


### 3. Constraints

Constraints can be equalities or inequalities - both are used interchangeably.



## What is linearity?

Linear:

- things always move the same direction.
- the same way is always up (or down).

You may come across the term *affine* - which is just a fancy way to say linear.

Non-linear:

- the correct direction to move depends on your current position.

If you have two variables (these are two things we can change to make our objective big or small):

$\textbf{V} = \begin{bmatrix}v_{1} \\ v_{2} \\ \end{bmatrix}$

You cannot do operations that are non-linear

- multipying a variable by itself $ v_{1}^{2} $
- multipying a variable by another variable $v_{1} * v_{2} $ (bilinearity)

We also cannot do conditional logic like `if`.


## What is optimization?

Making something small (like cost) or big (like profit) by changing variables (parameters, weights).


### Convex optimization

Not a useful concept when building programs but you may come across it.

There are two types - concave & convex.  Convex is the linear/easy one.

A linear program is a convex optimization problem:

- only one globally optimal solution (or infeasible).


## What makes optimization difficult?

Non-linearity - things changing direction based on where you are.

If there are gaps (discontinuities).


## The value of linearity in linear programming

Linear optimization gives us a gurantee that we can find the global optimum - the absolute best value of our variables.

Non-linear models don't give us this gurantee - making the optimization a noisy and stochastic process (see training neural nets or evolutionary algorithms).


## The cost of linearity in linear programming

Only model linear systems.

Much more work required, most problems have a few tricks to get interactions between variables.


Where can non-linearity come
- in the objective function
- in the constraints
- 
 
## What writing linear programs is like?

Along with requiring linearity, linear programs also require no discontinuities.  This means you cannot use conditionals like `if` in a linear program.

Lots of effort to keep the program linear

- can't use many things programmers rely on often, like conditional branching

Much of the skill in linear programs is being able to link variables to each other without non-linear operationsjjjaoeua


