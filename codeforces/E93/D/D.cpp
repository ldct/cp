#include <bits/stdc++.h>
using namespace std;

int R, G, B;
vector<int> red, green, blue;

long long memo[201][201][201];

long long max_dp(int r, int g, int b) {
  int count = (r == R) + (g == G) + (b == B);
  if (count == 3) return 0;

  if (memo[r][g][b] != -1) return memo[r][g][b];

  long long ret = 0;

  if (r != R && g != G) ret = max(ret, red[r]*green[g] + max_dp(r+1, g+1, b));
  if (r != R && b != B) ret = max(ret, red[r]*blue[b] + max_dp(r+1, g, b+1));
  if (g != G && b != B) ret = max(ret, blue[b]*green[g] + max_dp(r, g+1, b+1));

  return memo[r][g][b] = ret;
}

int main() {
  
  for (int i=0; i<201; i++) for (int j=0; j<201; j++) for (int k=0; k<201; k++) memo[i][j][k] = -1;

  cin >> R >> G >> B;

  int x;
  for (int i=0; i<R; i++) { cin >> x; red.push_back(x); }
  for (int i=0; i<G; i++) { cin >> x; green.push_back(x); }
  for (int i=0; i<B; i++) { cin >> x; blue.push_back(x); }

  sort(red.begin(), red.end()); reverse(red.begin(), red.end());
  sort(green.begin(), green.end()); reverse(green.begin(), green.end());
  sort(blue.begin(), blue.end()); reverse(blue.begin(), blue.end());

  cout << max_dp(0, 0, 0) << endl;

  return 0;
}
