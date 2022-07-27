#!/usr/bin/env python3

# left-aligned binary trie, struct-of-arrays
# similar speed in pypy as AoS but about 25% less memory

# cf custom test python 3.8: 46316 KB (46 MB)

class BinaryTrie_pool:
    def __repr__(self) -> str:
        return f"{self.num_words, self.starts, self.child0, self.child1}"

    def alloc(self):

        self.num_words += [0]
        self.starts += [0]
        self.child0 += [-1]
        self.child1 += [-1]

        self.next_alloc += 1
        return self.next_alloc - 1

    def __init__(self):

        self.num_words = []
        self.starts = []
        self.child0 = []
        self.child1 = []

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
 
if __name__ == '__main__':
    def bin(x):
        return "{0:b}".format(x)

    import random
    trie = BinaryTrie_pool()
    for _ in range(10**5):
        x = random.randint(1, 10**9)
        trie.insert(bin(x))
    print("done")