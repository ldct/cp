#include <bits/stdc++.h>
using namespace std;

constexpr size_t MAX_N = 10000009;

string S;
int ans[MAX_N];

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  
  int T;
  cin >> T;
  for (int i=0; i<T; i++) {
    cin >> S;

    int last_ans = -1;
    stack<int> unmatched_rbracket;

    int stack_base = 0;

    for(int p = S.size()-1; p >= 0; p--) {
      if (S[p] == ')') {
        ans[p] = last_ans;
        unmatched_rbracket.push(p);
      } else {
        if (unmatched_rbracket.size() > stack_base) {
          ans[p] = last_ans = unmatched_rbracket.top();
          unmatched_rbracket.pop();
        } else {
          ans[p] = last_ans = -1;
          stack_base = unmatched_rbracket.size();
        }
      }
    }

    int Q;
    cin >> Q;
    for (int j=0; j<Q; j++) {
      int q;
      cin >> q;
      auto r = ans[q-1];
      if (r != -1) r++;
      cout << r << endl;
    }
  }
    
  return 0;
}
