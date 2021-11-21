#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

long long ans(long long A, long long B, long long T) {
  B -= A; A = 0;
  long long free = min(T, 24-B);
  T -= free;
  if (T == 0) return 0;

  long long days = T / 24;
  long long extra_hours = T % 24;
  return days * B + min(extra_hours, B);
}

int main() {

  long long A, B, T;
  cin >> A >> B >> T;
  cout << ans(A, B, T) << endl;

  return 0;
}
