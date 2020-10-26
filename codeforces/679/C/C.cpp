#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

template<typename T>
class PQ {
public:
    multiset<T> s;

    int size() { return s.size(); }
    bool isEmpty() { return (s.size() == 0); }
    void insert(T x) { s.insert(x); }
    T getMin() { return *(s.begin()); }
    T getMax() { return *(s.rbegin()); }
    void deleteMin() {
      if (s.size() == 0) return;
      s.erase(s.begin());
    }
    void deleteMax() {
      if (s.size() == 0) return;
      auto it = s.end();
      it--;
      s.erase(it);
    }
};

long long a, b, c, d, e, f;
int N;
vector<vector<long long>> spans;

int main() {

  cin >> a >> b >> c >> d >> e >> f;

  cin >> N;

  for (int i=0; i<N; i++) {
    long long X;
    cin >> X;
    vector<long long> span;

    if (X - a >= 0) span.push_back(X-a);
    if (X - b >= 0) span.push_back(X-b);
    if (X - c >= 0) span.push_back(X-c);
    if (X - d >= 0) span.push_back(X-d);
    if (X - e >= 0) span.push_back(X-e);
    if (X - f >= 0) span.push_back(X-f);

    sort(span.begin(), span.end());
    reverse(span.begin(), span.end());
    spans.push_back(span);
  }


  PQ<pair<long long, int>> ws;

  for (int i=0; i<spans.size(); i++) {
    long long bk = spans[i].back();
    spans[i].pop_back();
    ws.insert(make_pair(bk, i));
  }

  long long ret = LLONG_MAX;
  while (1) {
    ret = min(ret, ws.getMax().first - ws.getMin().first);
    auto m = ws.getMin();
    ws.deleteMin();
    if (spans[m.second].size() == 0) break;
    ws.insert(
      make_pair(spans[m.second].back(), m.second)
    );
    spans[m.second].pop_back();
  }
  cout << ret << endl;

  return 0;
}
