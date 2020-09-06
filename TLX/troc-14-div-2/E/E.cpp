#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 20009;

long long N;
long long memo[MAX_N][15][15];

vector<long long> A;
vector<long long> B;

int main() {

  for (int i=0; i<MAX_N; i++) {
    for (int a=0; a<=10; a++) {
      for (int b=0; b<=10; b++) {
        memo[i][a][b] = -1;
      }
    }
  }

  cin >> N;

  for (int i=0; i<N; i++) {
    long long a;
    cin >> a;
    assert(0 <= a); assert(a <= 10);
    A.push_back(a);
  }

  for (int i=0; i<N; i++) {
    long long b;
    cin >> b;
    assert(0 <= b); assert(b <= 10);
    A.push_back(b);
  }

  sort(A.begin(), A.end());
  reverse(A.begin(), A.end());

  long long ret = 0;

  for (int i=0; i<N; i++) {
    ret += A[i];
  }

  cout << ret << endl;


}
