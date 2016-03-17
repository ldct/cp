#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long ll;

ll N, a, b, T;
string S;

const int MAX_N = 200000;

// number of w photos in [0, i)
int numWEnding[MAX_N+1]; 

int numW(int start, int end) {
  // num of w photos in the circular interval [start, end]
  if (start <= end) return numWEnding[end+1] - numWEnding[start];
  return numW(start, N-1) + numW(0, end);
}

int numSwipes(int start, int end) {
  // of swipes in the circular interval [start, end]
  if (start <= end) return end - start;
  return numSwipes(start, N) + numSwipes(0, end);
}

ll costView(int start, int end) {

  // cost to view the circular interval [start, end]
  int numPhotos = numSwipes(start, end) + 1;
  return numPhotos + b * numW(start, end);

}

int costUse(int start, int end) {

  // cost to use the interval [start, end] starting at element 0

  ll leftSwipes = numSwipes(start, 0);
  ll rightSwipes = numSwipes(0, end);

  ll numSwipes = 0;

  if (leftSwipes < rightSwipes) {
    numSwipes = 2 * leftSwipes + rightSwipes;
  } else {
    numSwipes = 2 * rightSwipes + leftSwipes;
  }

  return a*numSwipes + costView(start, end);
}

int main() {
  cin >> N >> a >> b >> T;
  getline(cin, S);
  getline(cin, S);
  // cout << S << endl;

  // fill up numWEnding
  numWEnding[0] = 0;
  for (int i=1; i<=N; i++) {
    numWEnding[i] = numWEnding[i-1];
    if (S[i-1] == 'w') numWEnding[i] += 1;
  }

  cout << numW(7, 4) << endl;

  // for (int i = 0; i < N; i++) {
  //   for (int j = 0; j < N; j++) {
  //     if (0 < i && i <= j) continue;
  //     if (costUse(i, j) <= T) {
  //       cout << "(" << i << " " << j << ")" << " " << numSwipes(i, j) + 1 << " " << costUse(i, j) << endl;
  //     }
  //   }
  // }

}
