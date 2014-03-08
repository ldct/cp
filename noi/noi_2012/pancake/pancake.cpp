#include <algorithm>
#include <map>
#include <queue>
#include <cstdio>

using namespace std;
typedef vector<int> vi;

int N;

void print_pancake(vi pancake) {
  for (vi::iterator i = pancake.begin(); i != pancake.end(); i++) {
    printf("%d ", *i);
  }
}

vi flipped_pancake(vi pancake, int position) {
  vi res = vector<int>();
  for (int i=0; i<position; i++) {
    res.push_back(pancake[i]);
  }
  for (int i=N-1; i>=position; i--) {
    res.push_back(pancake[i]);
  }
  return res;
}

bool is_sorted(vi pancake) {
  for (int i=0; i<N-1; i++) {
    if (pancake[i] < pancake[i+1]) return false;
  }
  return true;
}

int run_test(vi initial) {
  map<vi, int> dist;
  queue<vi> q;

  dist[initial] = 0;
  q.push(initial);

  while (!q.empty()) {
    vi u = q.front();
    q.pop();
    
    if (is_sorted(u)) {
      return dist[u];
    }

    for (int i=0; i<N-1; i++) {
      vi f = flipped_pancake(u, i);
      if (!dist.count(f)) {
        dist[f] = dist[u] + 1;
        q.push(f);
      }
    }
  }  
}

int main() {
  int T;
  scanf("%d", &T);

  while (T--> 0) {
    scanf("%d", &N);

    vi initial = vector<int>();
    for (int i=0; i<N; i++) {
      int size;
      scanf("%d", &size);
      initial.push_back(size);
    }

    printf("%d\n", run_test(initial));
  }
}