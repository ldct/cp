#include <cstdio>

#define MAX_N 17

int tree[1 << (MAX_N + 1)];

int main() {
  
  int N, M;

  scanf("%d %d", &N, &M);
  for (int i=0; i<(1<<N); i++) {
    scanf("%d", &tree[(1<<N) + i]);
  }
  int level = N;
  bool using_or = true;
  while (--level >= 0) {
    // populate the level at `level`
    for (int i=1<<level; i<1<<(level+1); i++) {
      if (using_or) {
        tree[i] = tree[2*i] | tree[2*i+1];
      } else {
        tree[i] = tree[2*i] ^ tree[2*i+1];
      }
    }
    using_or = !using_or;
  }
  for (int q=0; q<M; q++) {
    int p, b;
    scanf("%d %d", &p, &b);
    int index = (1<<N) + p - 1;
    using_or = true;
    tree[index] = b;
    index /= 2;
    while (index >= 1) {
      if (using_or) {
        tree[index] = tree[2*index] | tree[2*index+1];
      } else {
        tree[index] = tree[2*index] ^ tree[2*index+1];
      }
      using_or = !using_or;
      index /= 2;
    }
    printf("%d\n", tree[1]);
  }

  // for (int i=1; i < (1 << (N+1)); i++) {
  //   printf("%d ", tree[i]);
  // }
  // printf("\n");

  return 0;
}
