# Linear Programming

A half-day course on **linear programming** - a useful optimization technique.

Key outcomes of this course (things you should try to learn/remember):

- **the three components of a linear program**,
- what is linearity & why is it important,
- what makes a program non-linear.

After this lecture material we will do practical work together in [linear-programming.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/linear-programming/linear-programming.ipynb).


## Resources & Further Reading

Learn more about linear programming:

- [6 part blog post series on linear programming with PuLP - Ben Alex Keen](http://benalexkeen.com/blog/),
- [Michel Goemans lecture notes](https://math.mit.edu/~goemans/18310S15/lpnotes310.pdf),
- [Linear programming textbook by Thomas Ferguson](https://www.math.ucla.edu/~tom/LP.pdf),
- [Linear programming on Wikipedia](https://en.wikipedia.org/wiki/Linear_programming).
- [Linear programming tricks from the AIMMS Modeling Guide](https://download.aimms.com/aimms/download/manuals/AIMMS3OM_LinearProgrammingTricks.pdf)

Some of my own work:

- [dispatching electric battery storage](https://github.com/ADGEfficiency/energy-py-linear),
- [using linear programming to measure forecast accuracy](https://adgefficiency.com/energy-py-linear-forecast-quality/).


## Using linear programs to solve business problems

Writing linear programs requires two skills - the first is what prevents most linear programming business value from being achieved:

1. **identifying the business problem** can be modelled as a linear program,
2. writing the objective, variables and constraints of that program.

You won't need to write a solver, or understand how a linear programming solver works. 

You can be an effective driver without understanding the chemistry of combustion - **you can solve business problems without understanding the all math behind linear programming**.

The main math things to understand are:

1. what linearity is,
2. what a discontinuity is.

Experience will help you understand how to avoid both non-linearity & discontinuites in your programs.  If you can't, then you need a non-linear solver.


## What is writing linear programs like?

Restrictive compared to normal programming:

- lots of effort to keep the program linear,

Can't use many things programmers rely on often, like:

- multiplying variables together (non-linear),
- conditional branching `if` (discontinuous),
- taking the absolute value of a float (discontinuous).

Some of the skill in writing linear programs:

- being able to link variables to each other (without multiplying them together),
- transforming non-linear constraints/objective functions into linear constraints,
- knowing the tricks that are needed for your particular business problem (I've discovered most of mine from 1990's energy engineering papers),
- google `linear programming tricks` if you are interested.


## What is linear programming?

A **constrained optimization** method:

- minimize cost or maximize profit,
- under some constraints,
- by changing some variables.

Guaranteed to find the **global optimum**:

- other optimization methods don't have guarantees of finding a global optimum,
- will run deterministically, with no reliance on initial conditions.

Other optimization methods are either non-linear and/or unconstrained:

- non-linear programming - constrained, non-linear,
- stochastic gradient descent - unconstrained, non-linear,
- evolutionary optimization - unconstrained, non-linear.

Training neural networks:

- loss = highly non-linear,
- unconstrained = weights can take on any values,
- very sensitive to weight initialization.

For deep learning, we never find the global optimum for any large neural network loss surface - but local optima are 'good enough'.


## Why not linear programming?

Many problems are not linear:

- an energy balance (where both mass & energy are conserved) is non-linear.  Using LP in energy systems requires making a choice about what to balance (one of mass or energy).
- the efficiency of chillers can be non-linear.


## Three components of a linear program

1. **Objective function** - minimize or maximize,
2. **Variables** - things you can change - continuous, integer or binary,
3. **Constraints** - equality `==` or inequality `>=`, `<=`.

It is important to undertand that these  are the places where can non-linearity come in:

- in the objective function,
- in the constraints.

### 1. Objective function

Also called a cost function (loss in deep learning).

Represents what you want to do - can be either maximization or minimization.


### 2. Variables

Variables can be continuous, integer or binary - binary variables are often used as on/off variables.

A *mixed integer linear program* (MILP) is a linear program where some of the variables are integer - will require an MILP solver.

Most LP is MILP - integer & binary variables are useful to writing linear programs.


### 3. Constraints

Constraints can be equalities or inequalities - both are used interchangeably.


## What is optimization?

Making something small (like cost) or big (like profit) by changing variables (parameters, weights).

Local versus global optima - for a maximization problem:

![](assets/local.png)


Convex optimization
- not a useful concept when building programs (but you may come across it),
- there are two types - concave & convex, convex is the linear/easy one.

A linear program is a convex optimization problem - we are guaranteed to find the globally optimal solution (or infeasible/unbounded).


### What makes optimization difficult?

Non-linearity:

- the rate of change of direction changes depending on where you are.

Discontinuities:

- optimizers often take a hill-climbing type approach (SGD, Simplex, evolutionary algorihtms),
- climbing hills is hard if there are large ravines/gaps!


### What is linearity?

![](assets/nl.png)

Linear:

- the same way is always up/down,
- there is only one correct way to move up/down - it is always the same,
- you may come across the term *affine* (a fancy way to say linear).

Non-linear:

- which way is up/down depends on where you are,
- the correct direction to move depends on your current position.

If you have two variables (two things we can change to make our objective big or small):

$\textbf{V} = \begin{bmatrix}v_{1} \\ v_{2} \\ \end{bmatrix}$

You cannot do operations that are non-linear:

- multiplying a variable by itself $ v_{1}^{2} $,
- multiplying a variable by another variable $v_{1} * v_{2} $ (bilinear).

You cannot do operations that are discontinuous:

- conditional logic like `if`,
- absolute value.



## The value of linearity in linear programming

Linear optimization gives us a guarantee that we can find the global optimum - the absolute best value of our variables.

Non-linear models don't give us this guarantee - making the optimization a noisy and stochastic process (see training neural nets or evolutionary algorithms).


## The cost of linearity in linear programming

Only model linear systems.

Much more work required, most problems have a few tricks to get interactions between variables.


### Deep Dive - linking variables together

From A RIGOROUS MINLP MODEL FOR THE OPTIMAL SYNTHESIS AND OPERATION OF UTILITY PLANTS J. C. BRUNO, F. FERNANDEZ, F. CASTELLS and I. E. GROSSMANN (1998)

![](assets/bruno-1998.png)

Let's imagine we have an asset (such as a gas turbine, or GT) that can operate in the range of 50% to 100%.   We also have a cost function, which in normal programming would look like:

```
cost = gt_load * electric_efficiency * gas_price
```

It would be very easy to set the value of `gt_load` to be either 0 or 0.5 to 1.0 - it is not so easy in linear programs, because this is discontinuous!

One way to model this in a linear program would be with a continuous variable (we will use `puLP` to do this, but the idea holds for all linear programs):

```python
from pulp import LpVariable

load = LpVariable('gt-load-%', lowBound=0.5, upBound=1.0)
```

We would then have a term in the objective function representing the cost for running this unit:

```python
prob = LpProblem('min', LpMinimize)
prob += load * electric_efficiency * gas_price
```

What about if we wanted to model the gas turbine being off?  Currently we can't do this as our variable is constrained to a minimum of 50%.

Something like the below will allow our program to run the GT at 0% (ie off) - but also allow our GT to run at 25% load, which is not possible (many machines cannot operate below 40-50%).

```python
load = LpVariable('gt-load-%', lowBound=0.0, upBound=1.0)
```

One way to solve this problem is to introduce a second binary variable, that represents the GT being on `1` or off `0`:

```python
from pulp import LpVariable

load = LpVariable('gt-load-%', lowBound=0.5, upBound=1.0)
status = LpVariable('gt-load-%', cat='Binary')
```

We want the following two constraints in our program:

```
continuous - max * binary <= 0
- continuous + max * binary <= 0
```

The only way I can understand how these work is to create a table of 'what if' type scenarios.

Let's assume `max=1.0` and `min=0.5` (like our GT).

Let's explore the max equation first:

```
continuous - max * binary <= 0
```

| continuous | binary | LHS   | valid |
|------------|--------|-------|-------|
| 0.75       | 1.0    | -0.25 | Yes   |
| 1.0        | 1.0    | 0.0   | Yes   |
| 1.2        | 1.0    | 0.2   | No   |


I will leave it to the engaged & motivated reader to do the same exercise for:

- the minimum bound constraint,
- different values of the binary variable (for both constraints).

Now to the practical work in [linear-programming.ipynb](https://github.com/ADGEfficiency/teaching-monolith/blob/master/linear-programming/linear-programming.ipynb).

If you don't have Python installed locally, you can run this notebook [directly on Google Colab](https://githubtocolab.com/ADGEfficiency/teaching-monolith/blob/master/linear-programming/linear-programming.ipynb).
