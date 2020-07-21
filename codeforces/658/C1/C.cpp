#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }



vector<int> A;
vector<int> B;

void ans() {
  vector<int> ans;

  for (int i=A.size()-1; i != -1; i--) {
    cout << "considering " << A[0] << " " << A[i] << endl;
    if (A[i] == B[i]) {
      continue;
      // cout << "no need to fix " << A << B << "at " << i << endl; 
    }

    // cout << "fixing " << A << B << "at " << i << endl;

    // cout << "A=" << A << "i=" << i << endl;
    if (A[i] != A[0]) {
      ans.push_back(1);
      A[0] = 1 - A[0];
    }
    // cout << "A=" << A << endl;
    assert (A[i] == A[0]);
    ans.push_back(i+1);
    for (int j=0; j<(i+1)/2; j++) {
      swap(A[j], A[i-j]);
    }
    for (int j=0; j<=i; j++) {
      A[j] = 1-A[j];
    }

    // cout << "fixed, " << A << B << endl;
  }

  cout << ans.size();

  if (ans.size() > 0) cout << " ";
  
  for (int i=0; i<ans.size(); i++) { 
    cout << ans[i]; 
    if (i < ans.size() - 1) cout << " "; 
  }
  cout << endl;


}

int main() {
  
  int T;
  cin >> T;

  while (T --> 0) {
    int n;
    cin >> n;
    A.clear();
    B.clear();

    for (int i=0; i<n; i++) {
      char c;
      cin >> c;
      assert(c == '0' || c == '1');
      A.push_back(c == '0' ? 0 : 1);
    }

    for (int i=0; i<n; i++) {
      char c;
      cin >> c;
      assert(c == '0' || c == '1');
      B.push_back(c == '0' ? 0 : 1);
    }

    ans();
  }    
  return 0;
}
