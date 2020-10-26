#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

# TAG: linked list
class Event():
    def __init__(self, e):
        if e == '+':
            self.kind = '+'
            self.num = '?'
        else:
            self.kind = '-'
            self.num = int(e.split()[1])

        self.last = None
        self.next = set()

    def unset(self):
        for n in self.next:
            Event.events[n].last = self.last
            if self.last is not None:
                Event.events[self.last].next.add(n)

    def __repr__(self):
        return f"({self.kind}{self.num}, {self.last}, {self.next})"

    @classmethod
    def link(cls):
        events = cls.events

        last_plus_idx = None
        for i in range(len(events)):
            if events[i] == '+':
                if last_plus_idx is not None:
                    events[i].last = last_plus_idx
                    events[last_plus_idx].next.add(i)
                last_plus_idx = i
            else:
                if i-1 >= 0:
                    events[i].last = i-1
                else:
                    events[i].last = None
                events[i-1].next.add(i)

events = []
index_of = dict()

if False:
    N = int(input())
    for _ in range(2*N):
        e = input()
        events += [Event(e)]
else:
    N = 10000
    for _ in range(N):
        events += [Event("+")]
    for i in range(1, N+1):
        events += [Event(f"- {i}")]

for i, e in enumerate(events):
    if e.kind == '-':
        index_of[e.num] = i

def ans(events, index_of):
    Event.events = events
    Event.link()

    for i in range(1, N+1):
        e = events[index_of[i]]
        j = e.last
        if j is None:
            print("NO")
            return

        if events[j].kind != '+':
            print("NO")
            return

        if events[j].num != '?':
            print("NO")
            return

        events[j].num = i
        e.unset()
        events[j].unset()

    ret = []
    for e in events:
        if e.kind == '+':
            ret += [e.num]

    print("YES")
    print(*ret)





ans(events, index_of)
