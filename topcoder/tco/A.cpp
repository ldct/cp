#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

class EllysSortingTrimmer {
    public: string getMin(string S, int L) {
        S = rotate(S, S.length() - L, L);
        while (S.length() > L) {
            S = rotate(S, S.length() - L - 1, L);
            S = S.substr(0, S.length() - 1);
        }
        return S;
    }
    string rotate(string S, int i, int L) {
        sort(S.begin() + i, S.begin() + i + L);
        return S;
    }
};

int main() {
EllysSortingTrimmer ___test;
    cout << ___test.getMin("ESPRIT", 3);
}