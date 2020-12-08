#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

int N, M;
vector<long long> worms;
vector<long long> beaks;

bool ok(int k) {
  if (k == 0) return true;
  auto curr_pos = k-1;
  for (int i=0; i<N; i++) {
    if (curr_pos >= worms.size()) return false;
    if (worms[curr_pos] >= beaks[i]) return false;
    curr_pos += k;
  }
  return true;
}

int main() {
  cin >> N >> M;

  for (int i=0; i<N; i++) {
    long long b;
    cin >> b;
    beaks.push_back(b);
  }
  sort(beaks.begin(), beaks.end());

  int curr_ok = 0;

  vector<int> ret;

  for (int i=0; i<M; i++) {
    long long w;
    cin >> w;
    worms.push_back(w);
    sort(worms.begin(), worms.end());

    if (ok(curr_ok + 1)) curr_ok++;
    ret.push_back(curr_ok);
  }

  for (int i=0; i<ret.size(); i++) {
    cout << ret[i];
    if (i == ret.size() - 1) {
      cout << endl;
    } else {
      cout << " ";
    }
  }

  return 0;
}