#include <bits/stdc++.h>

#define MAX_N 1000001
#define MODULUS 1000000007

using namespace std;

int T, n, p;
unordered_set<int> used;

unsigned long long power(unsigned long long x, unsigned int y, int p) {  
    unsigned long long res = 1; 
    x = x % p;
   
    if (x == 0) return 0;
  
    while (y > 0) {  
        if (y & 1) res = (res*x) % p;  
  
        y = y>>1;
        x = (x*x) % p;  
    }  
    return res;  
}  

int ans() {
  vector<int> v;
  v.insert(v.end(), used.begin(), used.end());  

  sort(v.begin(), v.end());
  reverse(v.begin(), v.end());

  // for (int i=0; i<v.size(); i++) {
  //   printf("%d ", v[i]);
  // }
  // printf("\n");

  if (v.size() == 0) {
    return 0;
  }

  if (v.size() == 1) {
    return power(p, v[0], MODULUS);
  }

  // printf("adding %d ^ %d to first\n", p, v[0]);
  int first = power(p, v[0], MODULUS);
  int second = 0;
  for (int i=1; i<v.size(); i++) {
    // printf("adding %d ^ %d to second\n", p, v[i]);
    second += power(p, v[i], MODULUS);
    second = second % MODULUS;
  }

  if (p == 1) {
    return (second - first + MODULUS) % MODULUS;
  }
  return (first - second + MODULUS) % MODULUS;
}

int main() {  
  scanf("%d", &T);
  for (int t=0; t<T; t++) {
    used.clear();
    scanf("%d %d\n", &n, &p);
    for (int i=0; i<n; i++) {
      int ki;
      scanf("%d\n", &ki);
      if (used.count(ki) == 1) {
        used.erase(ki);
      } else {
        used.insert(ki);
      }
    }
    printf("%d\n", ans());
  }
  
  return 0;
}
