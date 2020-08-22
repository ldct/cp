#include <bits/stdc++.h>
using namespace std;

template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

constexpr size_t MAX_N = 500009;
int N;
long long value[MAX_N];
int resonates_with[MAX_N];

bool all_neg() {
  for (int i=0; i<N; i++) {
    if (resonates_with[i] != -1) return false;
  }
  return true;
}

long long score(vector<int>& order) {
  long long ret = 0;
  for (int i=0; i+1 < order.size(); i+=2) {
    auto idx1 = order[i];
    auto idx2 = order[i+1];

    idx1--; idx2--;

    if (resonates_with[idx1] == idx2+1) return LLONG_MAX;
    if (resonates_with[idx2] == idx1+1) return LLONG_MAX;

    ret += (i/2+1)*min(value[idx1], value[idx2]);
  }
  return ret;
}

void ST2() {
  assert(N <= 10);
  vector<int> order;
  for (int i=1; i<=N; i++) {
    order.push_back(i);
  }

  long long ret = LLONG_MAX;

  vector<int> argmin;

  do {
    auto r = score(order);
    if (r < ret) {
      argmin = order;
      ret = r;
    }
  } while (next_permutation(order.begin(), order.end()));

  if (ret == LLONG_MAX) {
    printf("-1\n");
    return;
  }
  printf("%lld\n", ret);

  for (int i=0; i+1 < argmin.size(); i+=2) {
    auto idx1 = argmin[i];
    auto idx2 = argmin[i+1];

    printf("%d %d\n", idx1, idx2);
  }
}

void ST3() {
  vector<pair<long long, long long>> v;
  for (int i=0; i<N; i++) {
    v.push_back({value[i], i+1});
  }
  sort(v.begin(), v.end());

  long long ret = 0;
  for (int i=0; i<N/2; i++) {
    long long p = N/2-i;
    p *= (long long)v[i].first;
    ret += p;
  }
  printf("%lld\n", ret);

  vector<pair<int, int>> correct_order;

  for (int i=0; i<N/2; i++) {
    correct_order.push_back({v[i].second, v[N/2 + i].second});
  }
  reverse(correct_order.begin(), correct_order.end());

  for (const auto& p : correct_order) {
    printf("%d %d\n", p.first, p.second);
  }
}

int main() {
  
  scanf("%d", &N);

  for (int i=0; i<N; i++) {
    scanf("%lld", &value[i]);
  }
  for (int i=0; i<N; i++) {
    scanf("%d", &resonates_with[i]);
  }

  if (all_neg()) {
    ST3();
    return 0;
  }
  if (N <= 10) {
    ST2();
    return 0;
  }

}
