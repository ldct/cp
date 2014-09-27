#include <string>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

class CandidatesSelectionEasy {
    public:
    vector<int> sort(vector<string> score, int x) {
        vector<pair<int, int> > skill_score;
        for (int i=0; i<score.size(); i++) {
            skill_score.push_back(make_pair((int)score[i][x], i));
        }

        std::sort(skill_score.begin(), skill_score.end());
        
        vector<int> ranks;
        for (int i=0; i<skill_score.size(); i++) {
            ranks.push_back(skill_score[i].second);
        }
        return ranks;
    }

};

// BEGIN CUT HERE
int main() {
CandidatesSelectionEasy test;
    //printf("%d\n", tests.minimalMoves("<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"));
}
// END CUT HERE