#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;
typedef vector<int> vi;

#define MAX_N 1000  
int N;
int V[MAX_N];
int W[MAX_N];

int f(vi coefficients) {
  int sum = 0;
  for (vi::iterator i = coefficients.begin(); i != coefficients.end(); i++) 
    sum += *i;
  int ss = sum * sum;
  int ssss = ss * ss;
  int res = ((ssss + 2 * ss) % 5) + 1;
  return res;
}

int sum_f(vi coefficients) {
  int i;
  /*
  for (i = 0; i < N; i++) {
    printf("%d ", coefficients[i]);
  }
  printf("\n");
  */
  for (i = 0; i < N; i++) {
    if (coefficients[i] == -1) {
      break;
    }
  }
  if (i == N) {
    return f(coefficients);
  } else {
    int ret = 0;
    for (int j=V[i]; j<=W[i]; j++) {
      coefficients[i] = j;
      ret += sum_f(coefficients);
      coefficients[i] = -1;
    }
    return ret;
  }
}

int main() {
  scanf("%d", &N);

  for (int i=0; i<N; i++) {
    scanf("%d %d", &V[i], &W[i]);
  }
  vi c = vi();
  for (int i=0; i<N; i++) {
    c.push_back(-1);
  }
  printf("%d\n", sum_f(c));
}
