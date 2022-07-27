#!/usr/bin/env python3
 
import io, os, sys
from sys import stdin, stdout
 
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())
 
from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache
import random
 
### CODE HERE

import sys
import array

class BinaryTrie_pool:
    def __repr__(self) -> str:
        return f"{self.num_words, self.starts, self.child0, self.child1}"

    def alloc(self):

        self.num_words.append(0)
        self.starts.append(0)
        self.child0.append(-1)
        self.child1.append(-1)

        self.next_alloc += 1
        return self.next_alloc - 1

    def __init__(self):

        self.num_words = array.array('L')
        self.starts = array.array('L')
        self.child0 = array.array('l')
        self.child1 = array.array('l')

        self.next_alloc = 0

        self.root = self.alloc()

    def anyChild(self, node):
        if self.child0[node] != -1 and self.starts[self.child0[node]] > 0:
            return self.child0[node]
        if self.child1[node] != -1 and self.starts[self.child1[node]] > 0:
            return self.child1[node]

    def insert(self, word):
        word = list(map(int, word))
        node=self.root
        for i in word:
            self.starts[node] += 1

            if i == 0 and self.child0[node] == -1: self.child0[node] = self.alloc()
            if i == 1 and self.child1[node] == -1: self.child1[node] = self.alloc()

            node = self.child0[node] if i == 0 else self.child1[node]
        self.num_words[node] += 1
        self.starts[node] += 1

    def findAnyWithPrefix(self, prefix):
        prefix = list(map(int, prefix))

        node = self.findNode(prefix)
        if node == -1 or node is None:
            return None
        if self.starts[node] == 0:
            return None
        while self.num_words[node] == 0:
            node = self.anyChild(node)
        return node

    def containsWord(self, word):
        word = list(map(int, word))
        node = self.findNode(word)
        if node == -1: return False
        return node.num_words > 0

    def remove(self, word):
        word = list(map(int, word))
        node=self.root
        self.starts[node] -= 1
        for i in word:
            if i == 0 and self.child0[node] == -1: return None
            if i == 1 and self.child1[node] == -1: return None

            node = self.child0[node] if i == 0 else self.child1[node]

            self.starts[node] -= 1
        self.num_words[node] -= 1

    def removeAnyWithPrefix(self, prefix):
        prefix = list(map(int, prefix))
        node=self.root
        for i in prefix:
            self.starts[node] -= 1
            node = self.child0[node] if i == 0 else self.child1[node]

        if self.num_words[node] > 0:
            self.starts[node] -= 1
            self.num_words[node] -= 1
            return 
        
        self.starts[node] -= 1

        while self.num_words[node] == 0:
            node = self.anyChild(node)
            self.starts[node] -= 1
        
        self.num_words[node] -= 1

    def findNode(self, word):
        word = list(map(int, word))
        
        node=self.root
        for i in word:
            if i == 0 and self.child0[node] == -1: return None
            if i == 1 and self.child1[node] == -1: return None

            node = self.child0[node] if i == 0 else self.child1[node]

        return node

    def startsWith(self, prefix):
        prefix = list(map(int, prefix))

        node = self.findNode(prefix)
        if node == -1: return False
        return self.starts[node] > 0
 
def clean(arr):
    ret = []
    for a in arr:
        x = a
        while x > 0 and x % 2 == 0:
            x //= 2
        ret += [x]
    return sorted(ret)[::-1]
 
def bin(x):
    return "{0:b}".format(x)
 
def ans(A, B):
    A = clean(A)
    B = clean(B)

    A = [bin(x) for x in A]
    B = [bin(x) for x in B]

    t = BinaryTrie_pool()

    for b in B:
        t.insert(b)
 
    for a in A:
        w = t.findAnyWithPrefix(a)
 
        if w is None:
            return "NO"

        t.removeAnyWithPrefix(a)
         
    return "YES"
 
if False:
    t = BinaryTrie_pool()
    t.insert("10")
    t.insert("100")
    print(t)
    print(t.anyChild(0))
else:
    for _ in range(read_int()):
        input()
        A = read_int_list()
        B = read_int_list()

        print(ans(A, B))
