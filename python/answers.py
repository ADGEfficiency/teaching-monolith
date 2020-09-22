import os

import requests
from bs4 import BeautifulSoup
import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, LpStatus


def store_biography_table(rows):
    out = []
    for row in rows:
        if row.find('th') and row.find('td'):
            out.append(
                {row.find('th').text: row.find('td').text}
            )

    #  clean unicode
    for row in out:
        for k, v in row.items():
            row[k] = v.replace('\xa0', '')
    return out


def all_external_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")

    table = soup.find_all('a')

    out = []
    for li in table:
        try:
            if li['class'] == ['external', 'text']:
                out.append(li)
        except:
            pass

    return out


def dl_img(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    imgs = soup.find_all('img')

    for img in imgs:
        if 'comic' in img['src']:
            img_url = 'https:' + img['src']
            print('found img at {}'.format(img_url))
            img_id = img_url.split('/')[-1]

    out_dir = './xckd'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, img_id), 'wb') as out:
        out.write(requests.get(img_url).content)

def find_next_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    links = soup.find_all('a')

    for l in links:
        try:
            if l['rel'] == ["prev"]:
                prev_url = l
                print('found {}'.format(l))
                break
        except:
            pass
    return 'https://xkcd.com/' + l['href']


def main():
    out_dir = os.path.join('.', 'images')
    url = 'https://xkcd.com/'
    for _ in range(5):
        dl_img(url)
        url = find_next_url(url)


def xckd_simple():
    urls = []
    for idx in range(1, 10):
        urls.append(
            'https://xkcd.com/{}/'.format(idx)
        )
    return urls


def transportation():
    port_capacity = [20, 30, 30, 50]
    market_demand = [20, 10, 5]

    #  one price for a port-market pair
    np.random.seed(42)
    port_cost = np.random.uniform(
        0, 1,
        size=len(port_capacity) * len(market_demand)
    )

    port_cost = port_cost.reshape(len(port_capacity), len(market_demand))

    #  variables
    var = []
    for port in range(len(port_capacity)):
        for market in range(len(market_demand)):
            var.append(LpVariable('p{}-m{}'.format(port, market), 0, None))

    var = np.array(var).reshape(len(port_capacity), len(market_demand))

    #  obj
    problem = LpProblem('minimization', LpMinimize)
    obj = []
    #  get the flow from port to market, along with the costs
    for trade, cost in zip(var.flatten(), port_cost.flatten()):
        obj.append(trade * cost)
    problem += sum(obj)

    #  constraints
    #  markets
    problem += sum(var[:, 0]) >= market_demand[0]
    problem += sum(var[:, 1]) >= market_demand[1]
    problem += sum(var[:, 2]) >= market_demand[2]

    # ports
    problem += sum(var[0, :]) <= port_capacity[0]
    problem += sum(var[1, :]) <= port_capacity[1]
    problem += sum(var[2, :]) <= port_capacity[2]
    problem += sum(var[3, :]) <= port_capacity[3]

    problem.solve()
    print(LpStatus[problem.status])

    for v in var.flatten():
        print('{} {}'.format(v.name, v.varValue))
