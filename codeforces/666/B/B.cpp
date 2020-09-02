#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> A;

void ans() {
  priority_queue<int> pq;
  for (const auto& a : A) {
    pq.push(a);
  }
  int banned = -1;

  int p1_turn = true;

  while (pq.size() > 0) {
    int pick = pq.top();
    pq.pop();
    assert(pick > 0);

    pick--;

    if (banned != -1) pq.push(banned);
    if (pick == 0) {
      banned = -1;
    } else {
      banned = pick;
    }
    p1_turn = !p1_turn;
  }

  if (p1_turn) { cout << "HL" << endl; } else { cout << "T" << endl; }

}
int main() {

  int T;
  cin >> T;

  while (T --> 0) {
    A.clear();
    cin >> N;
    for (int i=0; i<N; i++) {
      int a;
      cin >> a;
      A.push_back(a);
    }

    ans();

  }
    
  return 0;
}
