#include <cstdio>
#include <algorithm>
#include <string.h>
#include <math.h>

int N;

int max(int a, int b) {
    if (a > b) return a;
    return b;
}

int min(int a, int b) {
    if (a > b) return b;
    return a;
}

int cycle(int n) {
    if (n == 1)
        return 1;
    if (n % 2 == 0) {
        return 1 + cycle(n/2);
    }
    else {
        return 1 + cycle (3*n + 1);
    }
}

int main() {
    int i,j;
    while (scanf("%d %d", &i, &j) != EOF) {
        printf("%d %d", i, j);
        int max_cycle = -1;
        for (int x = min(i,j); x <= max(i,j); x++) {
            max_cycle = max(max_cycle, cycle(x));
        }
        printf(" %d\n", max_cycle);
    }
    return 0;
}
