#include <cstdio>
#include <map>
#include <cstring>

using namespace std;

#define MAX_N 200001

char s[MAX_N];

int ans() {
  int N = strlen(s);
  map<char, int> num;
  num['1'] = 0;
  num['2'] = 0;
  num['3'] = 0;

  int j = 0;
  while (j < N && (num['1'] == 0 || num['2'] == 0 || num['3'] == 0)) {
    num[s[j]]++;
    j++;
  }
  int i=0;
  while (num['1'] > 0 && num['2'] > 0 && num['3'] > 0) {
    num[s[i++]]--;
  }
  num[s[--i]]++;

  // printf("%d %d (%.*s) %d %d %d\n",i, j, j-i, s+i, num['1'], num['2'], num['3']);

  if (j == N) {
    if (num['1'] > 0 && num['2'] > 0 && num['3'] > 0) {
      return j-i;
    } else {
      return 0;
    }
  }

  int ans = j-i;
  while (j < N) {
    // printf("%d %d (%.*s) %d %d %d\n",i, j, j-i, s+i, num['1'], num['2'], num['3']);
    num[s[j++]]++;
    // printf("%d %d (%.*s) %d %d %d\n",i, j, j-i, s+i, num['1'], num['2'], num['3']);

    while (num['1'] > 0 && num['2'] > 0 && num['3'] > 0) {
      num[s[i++]]--;
    }
    // printf("%d %d (%.*s) %d %d %d\n",i, j, j-i, s+i, num['1'], num['2'], num['3']);
    num[s[--i]]++;
    // printf("%d %d (%.*s) %d %d %d\n",i, j, j-i, s+i, num['1'], num['2'], num['3']);
    ans = min(ans, j - i);
  }
  if (num['1'] > 0 && num['2'] > 0 && num['3'] > 0) {
    ans = min(ans, j - i);
  } 
  return ans;
}
int main() {
  
  int T;

  scanf("%d", &T);

  for (int t=0; t<T; t++) {
    scanf("%s\n", s);
    printf("%d\n", ans());    
  }

  return 0;
}
