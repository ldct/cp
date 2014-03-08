#include <cstdio>
#include <fstream>
#include <algorithm>
using namespace std;
#define MAX_N 1000

int N, A[MAX_N+1];

// return index of the first value in A that is >= v
int successor_index(int v) 
{
  int low=0, high=N, mid;
  while (low < high) {
    mid = (low + high) / 2;
    if (A[mid] < v) low = mid+1;
    else high = mid;
  }
  return low;
}

// count # of elements in [a,b]
int num_in_range(int a, int b)
{
  return successor_index(b+1) - successor_index(a);
}

int main(void)
{
  int answer = 0;
 
  scanf("%d", &N);
  for (int i=0; i<N; i++)
    scanf("%d", &A[i]);

  A[N] = 1000000000;
  sort(A,A+N+1);

  // Compute answer... O(N^2 log N)
  for (int i=0; i<N; i++)
    for (int j=i+1; j<N; j++) {
      int diff = A[j] - A[i];
      answer += num_in_range (A[j]+diff, A[j]+2*diff);
    }

  printf("%d\n", answer);
  return 0;
}