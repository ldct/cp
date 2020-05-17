#include <cstdio>
#include <algorithm>

#include <cassert>

using namespace std;

int ans_slow(int A, int B, int C, int D) {
    unsigned long long ret = 0;
    for (int x = A; x <= B; x++) for (int y = B; y <= C; y++) for (int z = C; z <= D; z++) {
        if (x + y > z && x + z > y && y + x > z) ret += 1;
    }
    return ret;
}

int num_x(int A, int B, int C, int D, int t) {
    int low = max(C - t, A);
    int high = min(B, D - t);

    return max(0, high - low + 1);
}

unsigned long long ans(int A, int B, int C, int D) {
    unsigned long long ret = 0;

    for (int t = 0; t <= D; t++) {
        int nx = num_x(A, B, C, D, t);
        int f = (C - max(B, t+1) + 1);
        if (nx > 0 && f > 0) {
            // printf("t = %llu nx = %llu f = %llu\n", t, nx, f);
            ret += nx * f;
        }
    }
    return ret;
}

void verify(int A, int B, int C, int D) {
    assert(ans(A, B, C, D) == ans_slow(A, B, C, D));
}

int main() {
  
    int A, B, C, D;

    scanf("%d %d %d %d", &A, &B, &C, &D);

    printf("%llu\n", ans(A, B, C, D));

    return 0;
}
