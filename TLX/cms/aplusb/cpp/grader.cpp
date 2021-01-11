#include "aplusb.h"

#include <cassert>
#include <cstdio>

int main() {
  int A, B;
  assert(2 == scanf("%d %d", &A, &B));

  printf("%d\n", add_two_numbers(A, B));
  return 0;
}
