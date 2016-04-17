#include <cstdio>
#include <cmath>

double epsilon = pow(10, -11);

double lg(double x) {
  return log(x) / log(2);
}

double a, b, d;

double f(double c) {
  return a * pow(b, c) + d * (1 + 1/c);
}

double fp(double c) {
  return a * log(b) * pow(b, c) - d / (c*c);
}

double root(double low, double high) {
  // f(low) < 0
  // f(high) > 0

  double mid = (high + low) / 2;

  if (fabs(high - low) < epsilon) {
    return mid;
  }

  if (fp(mid) > 0) {
    return root(low, mid);
  } else {
    return root(mid, high);
  }

}

int main() {

  double n, p, s, v;

  scanf("%lf %lf %lf %lf", &n, &p, &s, &v);

  a = n / (p * 1E9);
  b = pow(lg(n), sqrt(2));
  d = s / v;

  double min_c = root(1E-37, 1E37);
  printf("%.12lf %.12lf\n", f(min_c), min_c);


  return 0;
}
