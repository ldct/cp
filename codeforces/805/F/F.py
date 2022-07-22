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

class TrieNode:
    # Initialize your data structure here.
    def __init__(self, path):
        self.num_words = 0
        self.starts = 0
        self.children= dict()
        self.path = path

    def anyChild(self):
        for k in self.children:
            if self.children[k].starts > 0:
                return self.children[k]

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node=self.root
        for i in word:
            node.starts += 1
            if i not in node.children:
                node.children[i]=TrieNode(node.path+i)
            node=node.children[i]
        node.num_words += 1
        node.starts += 1

    def findAnyWithPrefix(self, prefix):
        node = self.findNode(prefix)
        if node is None:
            return node
        if node.starts == 0:
            return None
        while node.num_words == 0:
            node = node.anyChild()
        return node

    def search(self, word):
        node = self.findNode(word)
        if node is None: return False
        return node.num_words > 0

    def remove(self, word):

        if not (self.search(word)):
            while True:
                print("ohno")
        node=self.root
        node.starts -= 1
        for i in word:
            if i not in node.children:
                return None
            node=node.children[i]
            node.starts -= 1
        node.num_words -= 1

    def findNode(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                return None
            node=node.children[i]
        return node

    def startsWith(self, prefix):
        node = self.findNode(prefix)
        if node is None: return False
        return node.starts > 0
        

# Your Trie object will be instantiated and called as such:
trie = Trie()
words = Counter()
for _ in range(1000):
    rw = ''.join(random.choice("abc") for _ in range(random.randint(2, 5)))
    words[rw] += 1
    trie.insert(rw)

for k in words:
    while words[k] > 0:
        words[k] -= 1
        trie.remove(k)

 
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

    t = Trie()

    for b in B:
        t.insert(b)
 
    for a in A:
        w = t.findAnyWithPrefix(a)
 
        if w is None:
            return "NO"

        t.remove(w.path)
         
    return "YES"
 
if False:
    t = Trie()
    t.insert("11")
    t.insert('1001')

    t.remove("11")
    print(t.findAnyWithPrefix("11"))
elif False:
    A = [6, 6]
    B = [6, 9]
    print(ans(A, B))
elif False:
    for _ in range(1000000):
        N = random.randint(2, 2)
        A = [random.randint(1, 10) for _ in range(N)]
        B = [random.randint(1, 10) for _ in range(N)]
        print(A, B)
        print(ans(A, B))
else:
    for _ in range(read_int()):
        input()
        A = read_int_list()
        B = read_int_list()

        print(ans(A, B))
