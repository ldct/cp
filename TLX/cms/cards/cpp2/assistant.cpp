#include "assistant.h"

#include <bits/stdc++.h>

using namespace std;

void init_assistant(int N, int K) {
  assert(N <= 3);
  assert(K == 2);
}

vector<int> choose_cards(vector<int> cards) {
  assert(cards.size() == 2);
  sort(cards.begin(), cards.end());
  if (cards[0] == 1 && cards[1] == 2) return vector<int>({2});
  if (cards[0] == 2 && cards[1] == 3) return vector<int>({3});
  if (cards[0] == 1 && cards[1] == 3) return vector<int>({1});
  assert(0);
}
