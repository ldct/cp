#include <string>
#include <cstdio>

using namespace std;
class MagicalStringDiv2 {
    public:
    int minimalMoves(string S) {
    	int k = S.length() / 2;
    	int ret = 0;
    	for (int i=0; i<k; i++) {
    		if (S[i] != '>') ret++;
    	}
    	for (int i=k; i<2*k; i++) {
			if (S[i] != '<') ret++;
    	}
    	return ret;
    }

};

// BEGIN CUT HERE
int main() {
MagicalStringDiv2 ___test;
	printf("%d\n", ___test.minimalMoves("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"));
}
// END CUT HERE