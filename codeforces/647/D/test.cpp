#include <bits/stdc++.h>

using namespace std;

#define MAX_N 5000000

set<int> v[MAX_N];

int main() {  
  int ret = 0;

  for (int i=0; i<MAX_N; i++) {
    v[i].insert(i);
    ret += v[i].size();
    v[i].clear();
    ret += (1 - v[i].size());
  }

  printf("%d\n", ret);

  return 0;
}
