#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <queue>
#include <array>

// #include <bits/stdc++.h>


using namespace std;

int popcount(int x) { return bitset<32>(x).count(); }

int N;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

int highest_bit(uint64_t x) {
    return x == 0 ? -1 : 63 - __builtin_clzll(x);
}
 
template<int ALPHABET = 2>
struct BinaryTrie {
    struct trie_node {
        array<int, ALPHABET> child;
        int words = 0, starts_with = 0;
 
        trie_node() {
            memset(&child[0], -1, ALPHABET * sizeof(int));
        }
    };
 
    static const int ROOT = 0;
 
    vector<trie_node> nodes = {trie_node()};
 
    BinaryTrie(int total_length = -1) {
        if (total_length >= 0)
            nodes.reserve(total_length + 1);
    }
 
    int get_or_create_child(int node, int c) {
        if (nodes[node].child[c] < 0) {
            nodes[node].child[c] = int(nodes.size());
            nodes.emplace_back();
        }
 
        return nodes[node].child[c];
    }
 
    int build(uint64_t word, int delta) {
        int node = ROOT;
 
        for (int bit = highest_bit(word); bit >= 0; bit--) {
            nodes[node].starts_with += delta;
            node = get_or_create_child(node, int(word >> bit & 1));
        }
 
        nodes[node].starts_with += delta;
        return node;
    }
 
    int add(uint64_t word) {
        int node = build(word, +1);
        nodes[node].words++;
        return node;
    }
 
    int erase(uint64_t word) {
        int node = build(word, -1);
        nodes[node].words--;
        return node;
    }

    int down(int node) {
      return node;
      while (nodes[node].starts_with > nodes[node].words) {
        node = nodes[node].child[0];
      }
      return node;
    }
 
    int find(uint64_t query) const {
        int node = ROOT;
 
        for (int bit = highest_bit(query); bit >= 0; bit--) {
            node = nodes[node].child[query >> bit & 1];
 
            if (node < 0)
                break;
        }
 
        return node;
    }
 
    // Given a string, how many words in the trie are prefixes of the string?
    int count_prefixes(uint64_t query, bool include_full) const {
        int node = ROOT, count = 0;
 
        for (int bit = highest_bit(query); bit >= 0; bit--) {
            count += nodes[node].words;
            node = nodes[node].child[query >> bit & 1];
 
            if (node < 0)
                break;
        }
 
        if (include_full && node >= 0)
            count += nodes[node].words;
 
        return count;
    }
 
    // Given a string, how many words in the trie start with the given string?
    int count_starts_with(uint64_t query, bool include_full) const {
        int node = find(query);
 
        if (node < 0)
            return 0;
 
        return nodes[node].starts_with - (include_full ? 0 : nodes[node].words);
    }
};

void ans(vector<int>& A, vector<int>& B) {
    BinaryTrie S;

    for (auto b : B) {
      S.add(b);
    }

    sort(A.rbegin(), A.rend());

    // cout << A << B << endl;

    for (auto a : A) {
 
        if (S.count_starts_with(a, true)<= 0) {
          cout << "NO" << '\n';
          return;
        }
 
        S.erase(S.find(a));

    }
    cout << "YES" << endl;
}
int main() {

  int T;
  cin >> T;
  while (T --> 0) {
    cin >> N;
    
    vector<int> A;
    for (int i=0; i<N; i++) {
      int a;
      cin >> a;
      while (a > 0 && a % 2 == 0) { a /= 2; }
      A.push_back(a);
    }

    vector<int> B;
    for (int i=0; i<N; i++) {
      int b;
      cin >> b;
      while (b > 0 && b % 2 == 0) { b /= 2; }
      B.push_back(b);
    }

    ans(A, B);
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS