#!/usr/bin/python3

import random
def createRandomGraph():
    """Creates a digraph with 7 randomly chosen integer nodes from 0 to 9 and
    randomly chosen directed edges (between 10 and 20 edges)
    """
    g = {}
    n = random.sample([0,1,2,3,4,5,6,7,8,9], 7)
    for i in n:
        g[i] =[]
    edges = random.randint(10,20)
    count = 0
    while count < edges:
        a = random.choice(n)
        b = random.choice(n)
        if b not in g[a] and a != b:
            g[a].append(b)
            count +=1
    return g

def findPath(g, start, end, path=[]):
    """ Uses DFS to find a path between a start and an end node in g.
    If no path is found, returns None. If a path is found, returns the
    list of nodes """
    path = path + [start]
    if end == start:
        return path

    if not start in g:
        return None

    for node in g[start]:
        if node not in path:
            new_path = findPath(g, node, end, path)
            if new_path:
                return new_path
    return None


def allReachable(g, n):
    """
    Assume 'g' is a di-graph and 'n' is a node.
    Returns sorted list of all nodes such that there is a path from n to m in g.

    Input://
        g - graph
        n - node

    Returns://
        reachable_nodes - list of sorted nodes that are reachable from n.
    """
    # reachable_nodes = []
    # reachable_nodes = []
    # try:
    #     for i in g[n]:
    #         if i not in reachable_nodes:
    #             reachable_nodes.append(i)
    #         for x in g[i]:
    #             if findPath(g, i, x):
    #                 if x not in reachable_nodes:
    #                     reachable_nodes.append(x)
    # except KeyError:
    #     return []
    reachable_nodes = []
    available_nodes = list(g.keys())
    for i in available_nodes:
        if findPath(g, n, i):
            if i != n:
                reachable_nodes.append(i)

    return sorted(reachable_nodes)


g = createRandomGraph()
# a = findPath(g, 2, 5)
a = allReachable(g, 5)
print(a)
