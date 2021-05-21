#include "magician.h"

#include <bits/stdc++.h>

using namespace std;

void init_magician(int N, int K) {
  assert(N <= 3);
  assert(K == 2);
}

int find_discarded_card(std::vector<int> cards) {
  assert(cards.size() == 1);
  if (cards[0] == 2) return 1;
  if (cards[0] == 3) return 2;
  if (cards[0] == 1) return 3;
  assert(0);
}