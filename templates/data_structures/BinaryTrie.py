#!/usr/bin/env python3

# left-aligned binary trie

# cf python 3.8: 108016 KB (108 MB) 
# 
# (100 bytes / node)

import sys

class TrieNode:
    __slots__ = 'num_words', 'starts', 'child0', 'child1'

    def __init__(self):
        
        # getsizeof()=40

        self.num_words = 0
        self.starts = 0

        self.child0 = None
        self.child1 = None

    def anyChild(self):
        if self.child0 is not None and self.child0.starts > 0:
            return self.child0
        if self.child1 is not None and self.child1.starts > 0:
            return self.child1

class BinaryTrie:
    def __init__(self):

        self.root = TrieNode()

    def insert(self, word):
        word = list(map(int, word))
        node=self.root
        for i in word:
            node.starts += 1

            if i == 0 and node.child0 is None: node.child0 = TrieNode()
            if i == 1 and node.child1 is None: node.child1 = TrieNode()

            node = node.child0 if i == 0 else node.child1
        node.num_words += 1
        node.starts += 1

    def findAnyWithPrefix(self, prefix):
        prefix = list(map(int, prefix))

        node = self.findNode(prefix)
        if node is None:
            return node
        if node.starts == 0:
            return None
        while node.num_words == 0:
            node = node.anyChild()
        return node

    def containsWord(self, word):
        word = list(map(int, word))
        node = self.findNode(word)
        if node is None: return False
        return node.num_words > 0

    def remove(self, word):
        word = list(map(int, word))
        node=self.root
        node.starts -= 1
        for i in word:
            if i == 0 and node.child0 is None: return None
            if i == 1 and node.child1 is None: return None

            node = node.child0 if i == 0 else node.child1

            node.starts -= 1
        node.num_words -= 1

    def removeAnyWithPrefix(self, prefix):
        prefix = list(map(int, prefix))
        node=self.root
        for i in prefix:
            node.starts -= 1
            node = node.child0 if i == 0 else node.child1

        if node.num_words > 0:
            node.starts -= 1
            node.num_words -= 1
            return 
        
        node.starts -= 1

        while node.num_words == 0:
            node = node.anyChild()
            node.starts -= 1
        
        node.num_words -= 1

    def findNode(self, word):
        word = list(map(int, word))
        
        node=self.root
        for i in word:
            if i == 0 and node.child0 is None: return None
            if i == 1 and node.child1 is None: return None

            node = node.child0 if i == 0 else node.child1

        return node

    def startsWith(self, prefix):
        prefix = list(map(int, prefix))

        node = self.findNode(prefix)
        if node is None: return False
        return node.starts > 0

if __name__ == '__main__':
    print(sys.getsizeof(TrieNode()))
    def bin(x):
        return "{0:b}".format(x)

    import random
    trie = BinaryTrie()
    for _ in range(10**5):
        x = random.randint(1, 10**9)
        trie.insert(bin(x))
    print("done")