#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict

def hier(adj):

    deg = defaultdict(int)

    for u in adj:
        for v in adj[u]:
            deg[u] -= 1
            deg[v] += 1

    fake_u = None
    fake_v = None
    any_vertex = None

    for u in deg:
        any_vertex = u
        if deg[u] == -1: fake_v = u
        if deg[u] == 1: fake_u = u

    if fake_u == None:
        fake = None
    else:
        fake = [fake_u, fake_v]

    if fake is not None:
        adj[fake_u] += [fake_v]

    curr_path = []

    circuit = []

    # start from any vertex
    if fake_v is None:
        curr_path.append(any_vertex)
        curr_v = any_vertex
    else:
        curr_path.append(fake_v)
        curr_v = fake_v # Current vertex

    while len(curr_path):

        # If there's remaining edge,
        if len(adj[curr_v]):
            # Push the vertex
            curr_path.append(curr_v)
            # move to the next vertex using an edge and remove that edge
            curr_v = adj[curr_v].pop()

        # back-track to find remaining circuit
        else:
            circuit.append(curr_v)

            # Back-tracking
            curr_v = curr_path.pop()

    circuit = circuit[::-1]
    ret = []
    for i in range(len(circuit)-1):
        ret += [[circuit[i], circuit[i+1]]]

    if fake is None: return ret

    i = ret.index(fake)+1
    _ret = []
    for _ in range(len(ret)-1):
        _ret += [ret[i % len(ret)]]
        i += 1
    return _ret

def ans(pairs):
    neighbours = defaultdict(list)
    for u, v in pairs:
        neighbours[u] += [v]
    return hier(neighbours)

pairs = [[5,1],[4,5],[11,9],[9,4]]

print(ans(pairs))