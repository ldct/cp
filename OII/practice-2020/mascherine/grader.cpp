#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void riprogramma(int N, int K, vector<int>& C);

int main() {
  // ifstream cin("input.txt");
  // ofstream cout("output.txt");

  int N, K;
  cin >> N >> K;

  vector<int> C(N);
  for (int i = 0; i < N; i++) {
    cin >> C[i];
  }

  riprogramma(N, K, C);

  for (int i = 0; i < N; i++) {
    cout << C[i] << " ";
  }
  cout << endl;

  return 0;
}
