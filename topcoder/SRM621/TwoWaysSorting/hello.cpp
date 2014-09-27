#include <string>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

class TwoWaysSorting {
    public:
    string sortingMethod(vector <string> stringList) {
        bool sorted_by_length = true;
        bool sorted_lexicographic = true;
        for (int i=0; i<stringList.size() - 1; i++) {
            string s1 = stringList[i];
            string s2 = stringList[i+1];
            if (s1.size() > s2.size()) {
                sorted_by_length = false;
            }
            if (s1 > s2) {
                sorted_lexicographic = false;
            }
        }
        if (sorted_by_length && sorted_lexicographic) {
            return "both";
        }
        if (sorted_lexicographic) {
            return "lexicographically";
        }
        if (sorted_by_length) {
            return "lengths";
        }
        return "none";
    }

};

// BEGIN CUT HERE
int main() {
TwoWaySorting test;
    //printf("%d\n", tests.minimalMoves("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"));
}
// END CUT HERE