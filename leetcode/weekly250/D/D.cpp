#include <bits/stdc++.h>
using namespace std;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

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

class Solution {
public:
  vector<vector<int>> children;
  vector<vector<int>> queries;
  vector<unordered_map<int,int>> queries_at;

  int root;

  void dfs(int u, WordTrie& path) {
    // cout << "dfs " << u << "parent sz=" << path.size << endl;
    path.insert(u);
    for (auto& m : queries_at[u]) {
      queries_at[u][m.first] = ans(&path, m.first);
    }
    for (const auto v : children[u]) {
      dfs(v, path);
    }
    path.remove(u);
  }

  vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& _queries) {
    queries = _queries;

    children = vector<vector<int>>(parents.size()+10);
    queries_at = vector<unordered_map<int,int>>(parents.size()+10);

    for (const auto q : queries) {
      queries_at[q[0]][q[1]] = -1;
    }

    for (int i=0; i<parents.size(); i++) {
      if (parents[i] == -1) {
        root = i;
      } else {
        auto p = parents[i];
        children[p].push_back(i);
      }
    }

    WordTrie trie;;

    dfs(root, trie);

    vector<int> ret;
    for (const auto q : queries) {
      ret.push_back(queries_at[q[0]][q[1]]);
    }
    return ret;
  }
};

int main() {

  Solution s;
  vector<int> parents = {-1,0,1,1};
  vector<vector<int>> queries = {{0,2},{3,2},{2,5}};
  cout << s.maxGeneticDifference(parents, queries) << endl;;

  s = Solution();
  parents = {3,7,-1,2,0,7,0,2};
  queries = {{4,6},{1,15},{0,5}};
  // cout << s.maxGeneticDifference(parents, queries) << endl;;

  return 0;
}
