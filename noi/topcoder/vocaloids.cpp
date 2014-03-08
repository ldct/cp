#include <algorithm>
#include <cstdio>

#define P 1000000007

using namespace std;

int min3(int x, int y, int z) {
    return min(x, min(y, z));
}

int choose2(int N, int M, int a, int b);
int choose(int N, int a);

int choose3(int N, int a, int b, int c) {
    if (a + b + c < N) return 0;
    return choose(N, a) * choose2(N - a, a, b, c) % P;
}

int choose2(int M, int N, int a, int b) { //M cells must be occupied, N cells are up to you
    int ret = 0;
    for (int i=0; i<=M; i++) { //i a's take M cells, M-i b's take M cells,
        int x = choose(M, i);
        int y = choose(N, a-i);
        int z = choose(N, b-(M-i));
        ret = ret + (((x * y) % P) % z) % P;
    }
    return ret % P;
}

int choose(int N, int a) {
    if (N < 0) return 0;
    if (a < 0) return 0;
    if (a == 0) return 1;
    return choose(N-1, a) + choose(N-1, a-1) % P;
}

class VocaloidsAndSongs {
    public:
    int count(int S, int gumi, int ia, int mayu) {
        return choose3(S, gumi, ia, mayu);
    }

};

// BEGIN CUT HERE
int main() {
VocaloidsAndSongs ___test;
    //printf("%d\n", choose2(2,1,1,1));
	printf("%d\n", ___test.count(18,12,8,9));
}
// END CUT HERE