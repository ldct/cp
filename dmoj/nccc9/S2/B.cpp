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

template<typename T>
class PQ_del { /* max priority queue with deletion */
public:
  priority_queue<T> pq;
  priority_queue<T> deleted;

  T top() { return -pq.top(); }
  bool empty() { return pq.empty(); }
  bool size() { return pq.size() - deleted.size(); }
  void push(T e) { e = -e; pq.push(e); }
  void pop() { pq.pop(); }
  void remove(T e) {
    e = -e;
    if (!pq.empty() && pq.top() == e) {
      pq.pop();
      while (!pq.empty() && !deleted.empty() && pq.top() == deleted.top()) {
        pq.pop();
        deleted.pop();
      }
    } else {
      deleted.push(e);
    }
  }
};

class LeftIndexingBinaryList {
public:
  int floor = -1;
  PQ_del<int> indexes0, indexes1;
  vector<int> elems;
  LeftIndexingBinaryList(vector<int>& a) {
    elems = vector<int>(a.begin(), a.end());
    for (int i=0; i<elems.size(); i++) {
      if (elems[i] == 0) {
        indexes0.push(i);
      } else if (elems[i] == 1) {
        indexes1.push(i);
      } else {
        assert(false);
      }
    }
  }

  int find0(int start) {
    floor = start;
    while (!indexes0.empty() && indexes0.top() < floor) indexes0.pop();

    if (indexes0.empty()) return -1;
    // assert(indexes0.top() >= start);
    return indexes0.top();
  }

  int find1(int start) {
    floor = start;
    while (!indexes1.empty() && indexes1.top() < floor) indexes1.pop();

    if (indexes1.empty()) return -1;
    // assert(indexes1.top() >= start);
    return indexes1.top();
  }

  int find(int val, int start) {
    if (val == 0) return find0(start);
    if (val == 1) return find1(start);
    assert(false);
  }

  void swap(int i, int j) {
    if (elems[i] == elems[j]) return;
    if (elems[i] == 1) {
      indexes0.remove(j);
      indexes1.push(j);
      elems[i] = 0; elems[j] = 1;
    } else {
      indexes0.push(j);
      indexes1.remove(j);
      elems[i] = 1; elems[j] = 0;
    }
  }
};


long long ans(vector<int>& A, vector<int>& B) {
  long long ret = 0;
  int i = 0;
  auto _A = LeftIndexingBinaryList(A);
  while (i < A.size()) {
    if (_A.elems[i] == B[i]) {
      i += 1;
      continue;
    }
    int j = _A.find(B[i], i);
    if (j == -1) return -1;
    _A.swap(i, j);
    ret += (long long) (j - i);
  }
  return ret;
}

int main() {

  int N;
  char S[2000009];
  scanf("%d\n", &N);
  scanf("%s", S);

  vector<int> start, end;
  for (int i=0; i<2*N; i++) {
    end.push_back(i % 2);
    if (S[i] == 'I') {
      start.push_back(0);
    } else if (S[i] == 'U') {
      start.push_back(1);
    } else {
      assert(false);
    }
  }
  cout << ans(start, end) << endl;

  return 0;
}
