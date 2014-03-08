#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#define MAX_N 100000

using namespace std;

int N, height[MAX_N];
vector<int> peaks = vector<int>(0);
vector<int> valleys = vector<int>(0);

int main() {
  
  scanf("%d", &N);
  for (int i=0;i<N;i++) {
  	scanf("%d", &height[i]);
  }

  //(height[0] < height[1] ? valleys : peaks).push_back(height[0]);
  
  bool old_increasing = (height[0] < height[1]);
  for (int i=0;i<N;i++) {
  	bool now_increasing = (height[i] < height[i+1]);
  	if (now_increasing != old_increasing) {
  		(old_increasing ? peaks : valleys).push_back(height[i]);
  	}
  	old_increasing = now_increasing;
  }

  //(height[N-2] < height[N-1] ? peaks: valleys).push_back(height[N-1]);

  /*
  printf("peaks: ");
  for (vector<int>::iterator i = peaks.begin(); i != peaks.end(); i++) {
  	printf("%d ", *i);
  }

  printf("\n");

  printf("valleys: ");
  for (vector<int>::iterator i = valleys.begin(); i != valleys.end(); i++) {
  	printf("%d ", *i);
  }
  return 0;
  */

  vector<int>::iterator p = peaks.begin();
  vector<int>::iterator v = valleys.begin();

  int count = 1;
  int max_count = 1;
  while (p != peaks.end() || v != valleys.end()) {
  	max_count = max(max_count, count);
  	if (v == valleys.end() || (*p < *v && p != peaks.end())) { //next is peak
  		count--;
  		p++;
  	} else { //next is valley
  		count++;
  		v++;
  	}
  }
  printf("%d\n", max_count);

  return 0;
}
