#include <bits/stdc++.h>
using namespace std;

vector<int> mods = { 1000000007, 1000000009 };
seed_seq seq{(uint64_t) chrono::duration_cast<chrono::nanoseconds>(chrono::high_resolution_clock::now().time_since_epoch()).count(),(uint64_t) __builtin_ia32_rdtsc(),(uint64_t) (uintptr_t) make_unique<char>().get()};
mt19937 rng(seq);
int base = uniform_int_distribution<int>(1000, mods[0])(rng);

int main() {

  cout << base << endl;

  return 0;
}
