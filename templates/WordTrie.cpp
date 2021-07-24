#include <bits/stdc++.h>
using namespace std;

struct WordTrie { // 32-bit, >= 0
  int size = 0;
  int leaf = -1;
  WordTrie* zeros = nullptr;
  WordTrie* ones = nullptr;
  void insert(int word, int idx) {
    size++;
    if (idx == -1) {
      leaf = word;
      return;
    }
    int bit = (1 << idx) & word;
    if (bit == 0) {
      if (!zeros) zeros = new WordTrie;
      zeros->insert(word, idx-1);
    } else {
      if (!ones) ones = new WordTrie;
      ones->insert(word, idx-1);
    }
  }
  void remove(int word, int idx) {
    size--;
    if (idx == -1) {
      assert(leaf != -1);
      leaf = -1;
      return;
    }
    int bit = (1 << idx) & word;
    if (bit == 0) {
      assert(zeros);
      zeros->remove(word, idx-1);
    } else {
      assert(ones);
      ones->remove(word, idx-1);
    }
  }
  void insert(int word) { insert(word, 31); }
  void remove(int word) { remove(word, 31); }
};

bool exists(WordTrie* trie) {
  return trie && (trie->size > 0);
}

// max {query ^ w | w \in trie }
int ans(WordTrie* trie, int query) {
  if (trie->size == 0) return -1;
  for (int i=31; i>=0; i--) {
    assert(trie);
    assert(trie->size > 0);
    if (exists(trie->zeros) && !exists(trie->ones)) {
        trie = trie->zeros;
    } else if (exists(trie->ones) && !exists(trie->zeros)) {
        trie = trie->ones;
    } else {
        assert(exists(trie->ones));
        assert(exists(trie->zeros));
        assert(trie->size > 0);
        if ((1 << i) & query) {
            trie = trie->zeros;
        } else {
            trie = trie->ones;
        }
    }
  }
  // cout << "query=" << query << "size=" << trie->size << endl;
  // cout << "returning" << (query^trie->leaf) << endl;
  return query^trie->leaf;
}