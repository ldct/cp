#include <bits/stdc++.h>
using namespace std;

int N;

int match(string A, string B) {
  vector<int> pos;
  pos.push_back(-1);
  for (int i=0; i<N; i++) {
    if (A[i] == B[i]) continue;
    pos.push_back(i);
  }
  pos.push_back(N);

  int ret = 0;
  for (int i=0; i<((int)pos.size())-1; i++) {
    ret = max(ret, pos[i+1] - pos[i] - 1);
  }
  return ret;
}

char opp(char ha) {
  return ha == 'h' ? 'a' : 'h';
}

int main() {

  string S;

  cin >> N;
  cin >> S;
  string comp = "h";
  while (comp.size() < S.size()) {
    comp.push_back(opp(comp[comp.size()-1]));
  }

  int ret = match(S, comp);

  comp = "a";
  while (comp.size() < S.size()) {
    comp.push_back(opp(comp[comp.size()-1]));
  }
  ret = max(ret, match(S, comp));

  cout << ret << endl;

  return 0;
}
