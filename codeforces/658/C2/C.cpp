#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; os << "}"; }



vector<int> A;
vector<int> B;

void ans() {
  int left=0;
  vector<int> ans;

  bool has_swapped = false;

  for (int i=A.size()-1; i != -1; i--) {
    int a, aa;

    if (!has_swapped) {
      a = A[i]; aa = A[left];
    } else {
      aa = 1 - A[A.size() - left]; a = 1 - A[i + 1];
    }

    cout << "considering " << aa << " " << a << endl;

    if (a == B[i]) {
      continue;
    }
    left++;
    
    if (aa == B[i]) {
      ans.push_back(1);
    }
    ans.push_back(i+1);

    has_swapped = !has_swapped;
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
