#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>

using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

uint32_t log_2(const uint32_t x){if(x == 0) return 0;return (31 - __builtin_clz (x));}

int N;

i32 main() {

  cin >> N;
  cout << N << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS