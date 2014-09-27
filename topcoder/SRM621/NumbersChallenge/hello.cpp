#include <string>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
#include <iostream>

using namespace std;

class NumbersChallenge {
    public:
    int MinNumber(vector <int> S) {
        vector<int> formable;
        int N = S.size();
        for (int i=0; i < (1 << N); i++) {
            //cout << "considering subset " << i << " : ";
            int this_allowable = 0;
            for (int j=0; j<N; j++) {
                int mask = 1 << j;
                if ((mask & i) != 0) {
                    this_allowable += S[j];
                }
            }
            //cout << this_allowable << endl;
            formable.push_back(this_allowable);
        }
        sort(formable.begin(), formable.end());
        if (formable[0] > 1) {
            return formable[0];
        }
        for (int i=0; i<formable.size() - 1; i++) {
            if (formable[i] + 1 < formable[i + 1]) {
                return formable[i] + 1;
            }
        }
        return formable[formable.size() - 1] + 1;
    }

};

// BEGIN CUT HERE
int main() {
NumbersChallenge test;
vector<int> tv;

tv.push_back(2);
tv.push_back(1);
tv.push_back(2);
tv.push_back(7);
cout << test.MinNumber(tv);
}
// END CUT HERE