#include <string>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>

using namespace std;

class MixingColors {
    public:
    int minColors(vector<int> colors) {
        return iSet(colors).size();
    }

    vector<int> iSet(vector<int> S) {
        int N = S.size();
        for (int i=1; i < (1 << N); i++) {
            int sum = 0;
            int last_j;
            for (int j=0; j<N; j++) {
                int mask = 1 << j;
                if ((mask & i) != 0) {
                    last_j = j;
                    sum = sum ^ S[j];
                }
            }
            if (sum == 0) {
                S.erase(S.begin() + last_j);
                return iSet(S);
            }
        }
        return S;
    }
};

// BEGIN CUT HERE
int main() {
    MixingColors test;
    vector<int> tv;

    for (int i=0; i<23; i++) {
        tv.push_back(1 << i);
    }

    cout << test.minColors(tv);
}
// END CUT HERE