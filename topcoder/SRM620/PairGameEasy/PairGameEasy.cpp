#include <string>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>

using namespace std;

class PairGameEasy {
    public:
    string able(int a, int b, int c, int d) {
        return able_b(a, b, c, d) ? "Able to generate" : "Not able to generate";
    }
    map<pair<int, int>, bool> able_b_memo;
    bool able_b(int a, int b, int c, int d) {
        //(a,b) -> (c,d)
        if (a > c || b > d) {
            return false;
        } else if ((a == c) && (b == d)) {
            return true;
        } else if (able_b_memo.find(make_pair(a, b)) != able_b_memo.end()) {
            return able_b_memo[make_pair(a, b)];
        } else {
            able_b_memo[make_pair(a, b)] = (able_b(a+b, b, c, d) || able_b(a, a+b, c, d));
            return able_b_memo[make_pair(a, b)];
        }
    }

};

// BEGIN CUT HERE
int main() {
PairGameEasy test;
    cout << test.able(1,2,2,1);
}
// END CUT HERE