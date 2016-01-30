#include <iostream>
#include <cassert>
#include <vector>
#include <set>

using namespace std;

const int MAX_N = 1000000;

int N;
int spots[MAX_N];

vector<set<int> > neighbours;

void addRightNeighbours(int n) {
  for (int i = n+1; i < N; i++) {
    if (spots[n] + spots[i] == i-n) {
      neighbours[n].insert(i);
      neighbours[i].insert(n);
    }
  }
}

int main() {
  
  while (1) {
    cin >> N;

    if (N == 0) return 0;

    for (int i=0; i<N; i++) {
      cin >> spots[i];
      neighbours.push_back(set<int>());
    }

    for (int i=0; i<N; i++) {
      addRightNeighbours(i);
    }

    for (int i=0; i<N; i++) {
      cout << "neighbours[" << i << "] = ";

      for (auto it = neighbours[i].begin(); it != neighbours[i].end(); it++) {
        cout << *it << " ";
      }
      cout << endl;
    }

    cout << endl;

  }

}
