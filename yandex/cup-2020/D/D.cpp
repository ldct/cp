#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

struct PQ {
    multiset<long long> s;
    long long sum = 0;

    int size() { return s.size(); }
    bool isEmpty() { return (s.size() == 0); }
    void insert(long long x) { s.insert(x); sum += x; }
    long long getMin() { return *(s.begin()); }
    long long getMax() { return *(s.rbegin()); }
    void deleteMin() {
      if (s.size() == 0) return;
      sum -= getMin();
      s.erase(s.begin());
    }
    void deleteMax() {
      if (s.size() == 0) return;
      sum -= getMax();
      auto it = s.end();
      it--;
      s.erase(it);
    }
};
int N, K, R;

PQ front;
PQ back;

int main() {

  cin >> N >> K >> R;

  for (int i=0; i<K; i++) {
    long long x;
    cin >> x;
    front.insert(x);
  }

  for (int i=0; i<N-K; i++) {
    long long x;
    cin >> x;
    back.insert(x);
  }

  for (int i=0; i<R; i++) {
    long long a = front.sum;
    front.deleteMin();

    if (a <= back.getMin()) {
      front.insert(a);
    } else {
      back.insert(a);
    }

    while (front.size() != K) {
      front.insert(back.getMin());
      back.deleteMin();
    }
  }

  vector<long long> ret;

  for (const auto x : front.s) ret.push_back(x);
  for (const auto x : back.s) ret.push_back(x);

  sort(ret.begin(), ret.end());

  for (int i=0; i<ret.size(); i++) {
    cout << ret[i];
    if (i < ret.size()-1) cout << " ";
  }
  cout << endl;

  return 0;
}
