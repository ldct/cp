#include <algorithm>
#include <cstdio>

using namespace std;

int min3(int x, int y, int z) {
    return min(x, min(y, z));
}

int group2(int x, int y);

int group3(int x, int y, int z) {
    if (min3(x, y, z) > 0) {
        return 1 + group3(x - 1, y - 1, z - 1);
    }
    if (x == 0) return group2(y, z);
    if (y == 0) return group2(x, z);
    if (z == 0) return group2(x, y);
}

int group2(int x, int y) {
    if (min(x, y) > 0) {
        return 1 + group2(x - 1, y - 1);
    } else {
        return max(x, y); //return 1?
    }
}

class PackingBallsDiv2 {
    public:
    int minPacks(int R, int G, int B) {
        int ret = 0;

        int r = R % 3;
        int g = G % 3;
        int b = B % 3;

        return group3(r,g,b) + (R - r + G - g + B - b) / 3;
    }

};

// BEGIN CUT HERE
int main() {
PackingBallsDiv2 ___test;
	printf("%d\n", ___test.minPacks(2,3,3));
}
// END CUT HERE