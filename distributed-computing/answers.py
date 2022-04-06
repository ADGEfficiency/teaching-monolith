###  Create a data processing pipeline that selects the cities that have populations greater than the average of all cities

populations = [
    ('Berlin', 3.7, 'eu'),
    ('Auckland', 1.7, 'pac'),
    ('London', 8.9, 'eu'),
    ('Sheffield', 0.5, 'eu')
]

def avg(total, nxt):
    return (total[0]+nxt[1], total[1]+1)

total = reduce(avg, populations, (0, 0))

# total = tuple(sum, count)
mean = total[0] / total[1]

print(mean)
list(filter(lambda x: x.population > mean, populations))

#  You can also do this in a single reduce by incrementally updating the mean
# state = (mean, num)
def incremental_mean(state, nxt):
    state[1] += 1
    state[0] = state[0] + (nxt.population - state[0]) / state[1]
    return state

reduce(incremental_mean, populations, [0, 0])[0]

###  Create a data processing pipeline that finds the average population for both continents:
    
def gb(acc, city):
    acc[city.continent].append(city.population)
    return acc# acc is initialized as a dict here (see below)

pop_cont = reduce(
    gb,
    populations,
    {'eu': [], 'pac': []}
)

list(map(lambda kv: (kv[0], sum(kv[1]) / len(kv[1])), pop_cont.items()))