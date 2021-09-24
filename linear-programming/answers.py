import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, LpStatus


def transportation():
    problem = LpProblem("minimization", LpMinimize)

    ports = [20, 30, 30, 50]
    markets = [20, 10, 5]

    #  one price for a port-market pair
    np.random.seed(42)
    pm_cost = np.random.uniform(0, 1, size=len(ports) * len(markets))
    pm_cost = pm_cost.reshape(len(ports), len(markets))

    #  variables
    var = []
    for port in range(len(ports)):
        for market in range(len(markets)):
            var.append(LpVariable("p{}-m{}".format(port, market), 0, None))
    var = np.array(var).reshape(len(ports), len(markets))

    #  get the flow from each port to market, along with the costs
    obj = []
    for trade, cost in zip(var.flatten(), pm_cost.flatten()):
        obj.append(trade * cost)
    problem += sum(obj)

    #  constraints
    #  market demands
    problem += sum(var[:, 0]) >= markets[0]
    problem += sum(var[:, 1]) >= markets[1]
    problem += sum(var[:, 2]) >= markets[2]

    #  ports supplies
    problem += sum(var[0, :]) <= ports[0]
    problem += sum(var[1, :]) <= ports[1]
    problem += sum(var[2, :]) <= ports[2]
    problem += sum(var[3, :]) <= ports[3]

    problem.solve()
    print(LpStatus[problem.status])

    for v in var.flatten():
        print("{} {}".format(v.name, v.varValue))
