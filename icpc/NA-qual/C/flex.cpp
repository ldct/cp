#include <cstdio>
#include <set>
#include <vector>

using namespace std;

int main() {

  int W, P;
  int L[200];
  set<int> widths;

  scanf("%d %d", &W, &P);

  for (int i=0; i<P; i++) {
    scanf("%d", &L[i+1]);
  }
  L[0] = 0;
  L[P+1] = W;

  // for (int i=0; i < P+2; i++) {
  //   printf("%d ", L[i]);
  // }
  // printf("\n");

  for (int i=0; i < P + 2; i++) {
    for (int j=i+1; j < P + 2; j++) {
      // printf("%d %d %d\n", i, j, L[j] - L[i]);
      widths.insert(L[j] - L[i]);
    }
  }

  for (set<int>::iterator it=widths.begin(); it!=widths.end(); ++it) {
    printf("%d ", *it);
  }



  return 0;
}
