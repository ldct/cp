#include <bits/stdc++.h>

using namespace std;


constexpr int MODULUS = 1000000007;
constexpr int ZERO = 4000;

vector<int> m;

typedef std::tuple<int, int, int> iii;

struct key_hash : public std::unary_function<iii, std::size_t> {
 std::size_t operator()(const iii& k) const
 {
   auto h0 = hash<int>{}(get<0>(k));
   auto h1 = hash<int>{}(get<1>(k));
   auto h2 = hash<int>{}(get<2>(k));

   return h0^h1^h2;
 }
};

template < class T >
ostream& operator << (ostream& os, const vector<T>& v) {
    os << "[";
    for (auto& ii : v) {
        os << ii << ","; 
    }
    os << "]";
    return os;
}

map<iii,int> memo;

int dp(int n, int val, int k) {
  // number of ways to form `val` using a[0:n] using k -1's

  if (k < 0) return 0;

  if (val > 300) return 0;
  if (val < -300) return 0;

  if (n == 0) {
    if (val == 0 && k == 0) return 1;
    return 0;
  }

  iii key = {n, val, k};
  if (memo.count(key) > 0) {
    return memo[key];
  }

  auto ret = (dp(n-1, val, k) + dp(n-1, val-m[n-1], k) + dp(n-1, val+m[n-1], k-1)) % MODULUS;

  memo[key] = ret;

  return ret;

}

void ans(int N, int S, int K) {
  if (S > 300) {
    cout << 0 << endl;
    return;
  }

  int ret = 0;

  if (K > 100) K = 100;

  memo.clear();

  for (int k=0; k <= K; k++) {
    ret += dp(N,S,k);
  }
  cout << (ret % MODULUS) << endl;
}

int main() {
  
  m = vector<int>(100, 3);
  ans(100, 33, 100);
  cout << "size=" << memo.size() << endl;

  // int T;
  // cin >> T;
  
  // while (T --> 0) {
  //   int N;
  //   cin >> N;

  //   m.clear();

  //   for (int i=0; i<N; i++) {
  //     int mi;
  //     cin >> mi;
  //     m.push_back(mi);
  //   }

  //   int S, K;

  //   cin >> S >> K;

  //   ans(N, S, K);
  // }
}
