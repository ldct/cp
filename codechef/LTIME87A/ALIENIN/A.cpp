#include <bits/stdc++.h>
using namespace std;

constexpr double EPS = 1e-4;

int N;
long long D;
vector<long long> C;
priority_queue<pair<double, short>> worklist;

bool ok(double recharge_time) {

  worklist = priority_queue <pair<double, short>>();
  for (const auto c : C) {
    worklist.push({-c, -2});
    worklist.push({-(c + D), -1});
  }

  bool ready = true;
  int tokill = 0;
  int killed_not_expired = 0;

  while (worklist.size()) {
    auto p = worklist.top();
    worklist.pop();
    auto t = -p.first;

    if (p.second == -2) {
      if (ready) {
        // kill
        killed_not_expired++;
        ready = false;
        worklist.push({-(t + recharge_time), 0});
      } else {
        tokill++;
      }
    } else if (p.second == 0) { /* recharge */
      ready = true;
      if (tokill > 0) {
        // kill
        killed_not_expired++;
        ready = false;
        worklist.push({-(t + recharge_time), 0});
        tokill--;
      }
    } else {
      assert(p.second == -1);
      killed_not_expired--;
      if (killed_not_expired < 0) return false;
    }
  }

  return true;
}

int main() {
  
  int T;
  cin >> T;

  while (T --> 0) {
    C.clear();
    cin >> N >> D;
    for (int i=0; i<N; i++) {
      long long c;
      cin >> c;
      C.push_back(c);
    }

    double low = 0.0;
    double high = float(N+10)*float(D);

    assert(ok(low));
  	assert(!ok(high));

    long long count = 0;
    while (high - low > EPS) {
      count++;
  		double mid = (low + high) / 2;
      if (ok(mid)) {
  			low = mid;
      } else {
  			high = mid;
      }
    }
    cout << count << endl;
    cout << fixed << setprecision(8) << (low + high) / 2 << endl;
  }
  return 0;
}
