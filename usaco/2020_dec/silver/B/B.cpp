#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

struct BIT {
	vector<long long> s;
	BIT(int n) : s(n) {}
	void pointSet(int pos, long long dif) { // a[pos] += dif
		for (; pos < s.size(); pos |= pos + 1) s[pos] += dif;
	}
	long long rangeSum(int pos) { // sum of values in [0, pos)
		long long res = 0;
		for (; pos > 0; pos &= pos - 1) res += s[pos-1];
		return res;
	}
  long long rangeSum2(int a, int b) { // sum of values in [a, b]
    return rangeSum(b+1) - rangeSum(a);
  }
};

int N;
set<set<pair<int, int>>> allowed;

vector<pair<int, int>> coords;

int main() {

  vector<int> xs, ys;
  map<int, int> compressed_x_of;
  map<int, int> compressed_y_of;

  cin >> N;
  for (int i=0; i<N; i++) {
    int x, y;
    cin >> x >> y;
    xs.push_back(x); ys.push_back(y);
    coords.push_back({x, y});
  }

  sort(xs.begin(), xs.end());
  sort(ys.begin(), ys.end());


  for (int i=0; i<N; i++) {
    compressed_x_of[xs[i]] = i;
    compressed_y_of[ys[i]] = i;
  }

  for (int i=0; i<N; i++) {
    auto c = coords[i];
    coords[i] = {compressed_x_of[c.first], compressed_y_of[c.second]};
  }
  sort(coords.begin(), coords.end());

  // for (const auto c : coords) cout << c << endl;

  long long ans = 0;

  for (int i=0; i<N; i++) {

    auto bit = BIT(N+10);

    for (int j=i; j<N; j++) {
      auto a = coords[i];
      auto b = coords[j];

      bit.pointSet(b.second, 1);

      auto yl = min(a.second, b.second);
      auto yr = max(a.second, b.second);

      int left = bit.rangeSum2(0, yl);
      int right = bit.rangeSum2(yr, N+5);

      ans += left*right;
    }
  }

  cout << ans + 1 << endl;

  return 0;
}
