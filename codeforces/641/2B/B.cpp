#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_N 100002

int size[MAX_N];
int ans[MAX_N];

int main() {
  
  int T;

  scanf("%d", &T);

  for (int t=0; t<T; t++) {
    int N;
    scanf("%d\n", &N);
    for (int i=1; i<=N; i++) {
      scanf("%d", &size[i]);
      ans[i] = 1;
    }
    for (int i=1; i<=N; i++) {
      for (int j=2; i*j<=N; j++) {
        if (size[i] < size[i*j]) {
          ans[i*j] = max(ans[i*j], 1 + ans[i]);
        }
      }
    }
    int ret = -1;
    for (int i=1; i<=N; i++) {
      ret = max(ret, ans[i]);
    }
    printf("%d\n", ret);
  }
  
  return 0;
}
