#include <bits/stdc++.h>
using namespace std;

int popcount(int32_t x) { return bitset<32>(x).count(); }
int popcount(int64_t x) { return bitset<64>(x).count(); }