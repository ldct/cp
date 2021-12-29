#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

int N;
vector<int> H;

bool ok(int k) {
  vector<int> arr(H);

  for (int i=N-1; i>=2; i--) {
    if (arr[i] < k) return false;
    int d = (arr[i] - k) / 3;
    d = min(d, H[i] / 3);

    arr[i-2] += 2*d;
    arr[i-1] += d;
    arr[i] -= 3*d;
  }

  for (auto x : arr) {
    if (x < k) return false;
  }
  return true;
}

int ans() {

  int low = 0, high = 1e9+1;

  while (high - low > 2) {
    int mid = (low+high) / 2;
    if (ok(mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }

  for (int i=low; i<low+10; i++) {
    if (!ok(i)) return i-1;
  }
}

i32 main() {

  int T;
  cin >> T;

  while (T --> 0) {
    H.clear();
    cin >> N;
    for (int i=0; i<N; i++) {
      int h;
      cin >> h;
      H.push_back(h);
    }
    cout << ans() << endl;
  }

  return 0;
}
