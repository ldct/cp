#!/usr/bin/env pypy3

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

    def add_edge(self, u, v):
        self.neighbours[u].add(v)
        self.neighbours[v].add(u)

    def uncontractable_cycle(self):
        self.levels = dict()
        self.parent_of = dict()

        for v in range(1, self.N+1):
            if self.colours[v] == Graph.WHITE:
                r = self._uncontractable_cycle(v, v, 0)
                if r is not None: return r

        return None
        
    @bootstrap
    def _uncontractable_cycle(self, parent, u, level):
        self.levels[u] = level
        self.colours[u] = Graph.GREY
        self.parent_of[u] = parent

        back_edges = []
        
        for v in self.neighbours[u]:
            if v == parent: continue
            if self.colours[v] == Graph.GREY:
                back_edges += [(self.levels[u] - self.levels[v], (u, v))]

        if len(back_edges):
            (_, (u, v)) = sorted(back_edges)[0]
            cycle = [u]

            while True:
                if cycle[-1] == v: break
                cycle += [self.parent_of[cycle[-1]]]

            yield cycle
            return 

        for v in self.neighbours[u]:
            if v == parent: continue
            if self.colours[v] == Graph.WHITE:
                r = yield self._uncontractable_cycle(u, v, level+1)
                if r is not None:
                    yield r
            else:
                continue

        self.colours[u] = Graph.BLACK

        yield None
