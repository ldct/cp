#include <vector>
#include <iostream>
#include <map>
#include <climits>
#include <set>
#include <algorithm>
#include <array>
#include <cstring>
#include <unordered_map>

using namespace std;
#define int long long
#define i32 int32_t
#define i64 int64_t

typedef struct _Entry {
  int val;
  int prev;
} Entry;
Entry entries[500009];

unordered_map<int, int> notebook;

int curr = 0;
int next_idx = 1;
int alloc_entry(int val, int prev) {
  auto ret = next_idx;
  next_idx++;
  entries[ret].prev = prev;
  entries[ret].val = val;
  return ret;
}

int Q;

int add(int x) {
  curr = alloc_entry(x, curr);
  return x;
}

int k_delete() {
  curr = entries[curr].prev;
  return entries[curr].val;
}

int save(int y) {
  notebook[y] = curr;
  return entries[curr].val;
}

int load(int z) {
  curr = notebook[z];
  return entries[curr].val;
}

i32 main() {

  cin.tie(0);

  entries[0].val = -1;
  entries[0].prev = 0;

  int next = 1;

  int Q;
  cin >> Q;

  while (Q --> 0) {
    string cmd;
    cin >> cmd;
    if (cmd == "ADD") {
      int x; cin >> x;
      cout << add(x) << " ";
    } else if (cmd == "DELETE") {
      cout << k_delete() << " ";
    } else if (cmd == "SAVE") {
      int y; cin >> y;
      cout << save(y) << " ";
    } else if (cmd == "LOAD") {
      int z; cin >> z;
      cout << load(z) << " ";
    } else {
      cout << "?" << cmd << "?" << endl;
    }
  }
  cout << endl;

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS