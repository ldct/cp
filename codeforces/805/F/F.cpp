#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <queue>

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

struct Trie { // 32-bit, >= 0
  int size = 0;
  int leaf = -1;
  Trie* zeros = nullptr;
  Trie* ones = nullptr;
  void insert(int word, int idx) {
    size++;
    if (idx == -1) {
      leaf = word;
      return;
    }
    int bit = (1 << idx) & word;
    if (bit == 0) {
      if (!zeros) zeros = new Trie;
      zeros->insert(word, idx-1);
    } else {
      if (!ones) ones = new Trie;
      ones->insert(word, idx-1);
    }
  }
  bool contains(int word, int idx) {
    if (size == 0) return false;
    if (idx == -1) {
      return false;
    }
    int bit = (1 << idx) & word;
    if (bit == 0) {
      if (zeros) {
        return zeros->contains(word, idx-1);
      } else {
        return false;
      }
    } else {
      if (ones) {
        return ones->contains(word, idx-1);
      } else {
        return false;
      }
    }
  }
  void insert(int word) { insert(word, popcount(word)-1); }
  bool contains(int word) { return contains(word, popcount(word)-1); }

};

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

    cout << A << B << endl;

    Trie S;

    for (auto b : B) {
      S.insert(b);
    }

    sort(A.begin(), A.end());
    reverse(A.begin(), A.end());
    

    cout << S.size << endl;
    cout << S.zeros << endl;
    cout << S.ones << endl;

    cout << A << endl;
    cout << "S.contains(1)" << S.contains(1) << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS