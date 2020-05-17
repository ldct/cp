#include <cstdio>
#include <algorithm>

#include <cassert>

#define MAX_N 1000001

int ans[MAX_N];

using namespace std;

int main() {
  
    int N, S;

    scanf("%d %d", &N, &S);

    int s = S;
    for (int i=0; i<N; i++) {
        ans[i] = 1;
        s -= 1;
    }

    if (s < 0) {
        printf("NO\n");
        return 0;
    }

    ans[N-1] += s;

    int low = S - ans[N-1];
    int high = ans[N-1];

    if (high - low <= 1) {
        printf("NO\n");
        return 0;
    }

    int K = low + 1;

    printf("YES\n");
    for (int i=0; i<N; i++) {
        printf("%d ", ans[i]);
    }
    printf("\n");
    printf("%d\n", K);
    
    return 0;
}
