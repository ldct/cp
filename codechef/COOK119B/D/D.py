#!/usr/bin/env pypy3

from collections import defaultdict
from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

class Graph:

    WHITE = 0
    GREY = 1
    BLACK = 2
    
    def __init__(self, N):
        self.N = N
        self.colours = dict()
        self.neighbours = dict()

        for v in range(1, N+1):
            self.neighbours[v] = set()
            self.colours[v] = Graph.WHITE

    @classmethod
    def line(self, N):
        g = Graph(N)
        for i in range(1, N):
            g.add_edge(i,i+1)
        return g

    def add_directed_edge(self, u, v):
        self.neighbours[u].add(v)

    def add_edge(self, u, v):
        self.neighbours[u].add(v)
        self.neighbours[v].add(u)

    def cc(self):
        self.levels = dict()
        self.parent_of = dict()
        self.daddy_of = dict()

        for v in range(1, self.N+1):
            if self.colours[v] == Graph.WHITE:
                r = self.dfs(v, v, v, 0)

        return None

    def uncontractable_cycle(self):
        self.levels = dict()
        self.parent_of = dict()

        for v in range(1, self.N+1):
            if self.colours[v] == Graph.WHITE:
                r = self.dfs(v, v, v, 0)
                if r is not None: return r

        return None
        
    @bootstrap
    def dfs(self, daddy, parent, u, level):
        # self.levels[u] = level
        self.colours[u] = Graph.GREY
        # self.parent_of[u] = parent
        self.daddy_of[u] = daddy

        # back_edges = []
        
        # for v in self.neighbours[u]:
        #     if v == parent: continue
        #     if self.colours[v] == Graph.GREY:
        #         back_edges += [(self.levels[u] - self.levels[v], (u, v))]

        # if len(back_edges):
        #     (_, (u, v)) = sorted(back_edges)[0]
        #     cycle = [u]

        #     while True:
        #         if cycle[-1] == v: break
        #         cycle += [self.parent_of[cycle[-1]]]

        #     yield cycle
        #     return 

        for v in self.neighbours[u]:
            if v == parent: continue
            if self.colours[v] == Graph.WHITE:
                r = yield self.dfs(daddy, u, v, level+1)
                if r is not None:
                    yield r
            else:
                continue

        self.colours[u] = Graph.BLACK

        yield None


from fractions import Fraction

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

T = int(input())

def ans(g, ok_nodes):
    # print the largest connected component
    g.cc()

    cc_of = dict()

    for i in g.daddy_of:
        if i not in ok_nodes: continue
        if g.daddy_of[i] not in cc_of: cc_of[g.daddy_of[i]] = set()
        cc_of[g.daddy_of[i]].add(i)

    max_cc_size = max(map(len, cc_of.values()))

    max_cc = None

    for i in cc_of:
        if len(cc_of[i]) == max_cc_size:
            max_cc = cc_of[i]
            break
    
    assert(max_cc is not None)

    print(len(max_cc))
    print(' '.join(map(str, max_cc)))

for _ in range(T):
    [N, M, *rest] = input().split(' ')
    N = int(N)
    M = int(M)

    A = input().split(' ')
    A = [int(a) for a in A if len(a)]

    B = input().split(' ')
    B = [int(b) for b in B if len(b)]

    incomes = [Fraction(a, b) for a, b in zip(A, B)]
    max_income = max(incomes)

    ok_nodes = set()

    for i in range(1,N+1):
        if incomes[i-1] == max_income:
            ok_nodes.add(i)

    g = Graph(N)

    neighbours = dict()
    for i in range(1, N+1):
        neighbours[i] = set()

    for _ in range(M):
        [u, v, *rest] = input().split(' ')
        u = int(u)
        v = int(v)

        if not min(incomes[u-1], incomes[v-1]) == max_income:
            continue 

        g.add_edge(u, v)

    ans(g, ok_nodes)
