#include <cstdio>
#include <set>
#include <iostream>
#include <cmath>

using namespace std;

int M, H1, A1, X1, Y1, H2, A2, X2, Y2;

long long steps_to(long long x, long long y, long long curr, long long end, long long M) {

  long long steps = 0;
  while (curr != end) {
    if (steps++ > M) return -1;
    curr = (x * curr + y) % M;
  }
  return steps;
}

long long cycles(long long x, long long y, long long start, long long M) {

  long long ret = steps_to(x, y, (x * start + y) % M, start, M);
  if (ret == -1) return -1;
  return 1 + ret;

}

long long min_t(long long a, long long b, long long c) {
  // minimum value of t = a + bp = c

  if (a > c) return -1;
  if (a == c) return a;
  // bp = c - a > 0
  if (b == 0) return -1;
  if ((c - a) % b == 0) return c;
  return -1;

}

long long min_t(long long a, long long b, long long c, long long d) {

  // mininmum value of t = a + bp = c + dq
  // where p, q > 0 are integers

  if ((a == -1) || (c == -1)) return -1;
  if (a == c) return a;
  if (a < c) return min_t(c, d, a, b);
  if ((b == -1) && (d == -1) && (a != b)) return -1;
  // a > c
  if (d == -1) return min_t(a, b, c);
  if (b == -1) return min_t(c, d, a);


  // a - c + bp = dq
  // d | a - c + bp
  long long min_p = steps_to(1, b, (a - c) % d, 0, d);

  if (min_p == -1) return -1;
  return a + b * min_p;

}

int main() {

  scanf("%d\n %d %d\n %d %d\n %d %d\n %d %d", &M, &H1, &A1, &X1, &Y1, &H2, &A2, &X2, &Y2);

  long long a = steps_to(X1, Y1, H1, A1, M);
  long long b = cycles(X1, Y1, A1, M);
  long long c = steps_to(X2, Y2, H2, A2, M);
  long long d = cycles(X2, Y2, A2, M);

  // cout << a << " " << b << " " << c << " " << d << endl;

  cout << min_t(a, b, c, d) << endl;

  return 0;
}
