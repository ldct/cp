#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

ll N, a, b, T;
string S;

ll numSwipe(int start, int end) {
  // cost to swipe the interval [start, end]

  if (start == end) return 0;
  if (start < end) return (end - start);
  if (start > end) return numSwipe(start, N) + numSwipe(0, end);
  return -1;
}

int costView(int start, int end) {

  // cost to view the interval [start, end]

  ll cv = 0;

  int i = start;

  while (1) {
    cv += 1;
    if (S[i] == 'w') cv += b;
    if (i == end) break;
    i = (i + 1) % N;
  }

  ll leftSwipes = numSwipe(start, 0);
  ll rightSwipes = numSwipe(0, end);

  ll numSwipes = 0;

  if (leftSwipes < rightSwipes) {
    numSwipes = 2 * leftSwipes + rightSwipes;
  } else {
    numSwipes = 2 * rightSwipes + leftSwipes;
  }

  return a*numSwipes + cv;
}

int main() {
  cin >> N >> a >> b >> T;
  getline(cin, S);
  getline(cin, S);
  cout << S << endl;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (0 < i && i <= j) continue;
      if (costView(i, j) <= T) {
        cout << "(" << i << " " << j << ")" << " " << numSwipe(i, j) + 1 << " " << costView(i, j) << endl;
      }
    }
  }

}
