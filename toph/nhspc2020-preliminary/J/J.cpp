#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }

constexpr size_t MAX_N = 1001;
constexpr long long MAX_X = 16000000;

int N, Q;


pair<int,int> matrix[MAX_N][MAX_N];
long long filled_matrix[MAX_N][MAX_N];

vector<char> is_prime(MAX_X+1, true);

vector<pair<int,int>> spiralOrder() {
  int ir, ic;
  vector<vector<int> > dirs;

  vector<int> RIGHT = {1, 0};
  vector<int> DOWN = {0, 1};
  vector<int> LEFT = {-1, 0};
  vector<int> UP = {0, -1};

  if (N % 2 == 0) {
    dirs = {RIGHT, DOWN, LEFT, UP};
    ir = 0, ic = 0;
  } else {
    dirs = {LEFT, UP, RIGHT, DOWN};
    ir = N-1, ic = N-1;
  }
  ir -= dirs[0][0];
  ic -= dirs[0][1];
    

  vector<pair<int,int>> res;
  
  vector<int> nSteps{N, N-1};
  
  int iDir = 0;   // index of direction.
  while (nSteps[iDir%2]) {
      for (int i = 0; i < nSteps[iDir%2]; ++i) {
          ir += dirs[iDir][0]; ic += dirs[iDir][1];
          res.push_back(matrix[ic][ir]);
      }
      nSteps[iDir%2]--;
      iDir = (iDir + 1) % 4;
  }
  return res;
}

void sieve() {
  is_prime[0] = is_prime[1] = false;
  for (int i = 2; i <= MAX_X; i++) {
    if (is_prime[i] && (long long)i * i <= MAX_X) {
      for (int j = i * i; j <= MAX_X; j += i)
        is_prime[j] = false;
    }
  }
}

vector<long long> primes() {
  sieve();
  vector<long long> ret;
  for (int i=0; i<MAX_X; i++) {
    if (is_prime[i]) ret.push_back(i);
  }
  return ret;
}

int main() {
  
  cin >> N >> Q;

  for (int i=0;i<N; i++) {
    for (int j=0; j<N; j++) {
      matrix[i][j] = {i, j};
    }
  }

  auto order = spiralOrder();
  reverse(order.begin(), order.end());

  auto p = primes();
  
  for (int i=0; i<order.size(); i++) {
    auto xy = order[i];
    auto x = xy.first;
    auto y = xy.second;
    filled_matrix[x][y] = p[i];
  }

  for (int i=0; i<Q; i++) {
    int x,y;
    cin >> x >> y;
    x--; y--;
    cout << filled_matrix[x][y] << endl;
  }

  // for (int i=0; i<N; i++) {
  //   for (int j=0; j<N; j++) {
  //     cout << filled_matrix[i][j] << "\t";
  //   }
  //   cout << endl;
  // }

  return 0;

  for (int i=0; i<Q; i++) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    cout << filled_matrix[x][y] << endl;
  }

  cout << "order=" << order << endl;

  return 0;
}
