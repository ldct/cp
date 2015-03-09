#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, int> kattis_results;

int main() {

  int N;
  cin >> N;

  string s;
  getline(cin, s); //consume newline

  for (int i=0; i<N; i++) {
    getline(cin, s);

    if (kattis_results.find(s) == kattis_results.end()) {
        kattis_results[s] = 0;
    }
    kattis_results[s] += 1;

  }

  int matches = 0;

  for (int i=0; i<N; i++) {
    getline(cin, s);

    if (kattis_results.find(s) != kattis_results.end()) {
        if (kattis_results[s] > 0) {
            kattis_results[s]--;
            matches++;
        }
    }

  }

  cout << matches << endl;

  return 0;
}
