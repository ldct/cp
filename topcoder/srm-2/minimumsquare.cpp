#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <climits>
#include <algorithm>

using namespace std;
class MinimumSquareEasy {
    public:
    long long minArea(vector <int> x, vector <int> y) {
        int N = x.size();

        long long min_area = LLONG_MAX;

        for (int i=0; i < N; i++) {
            vector<int> x_p = x;
            vector<int> y_p = y;
            x_p.erase(x_p.begin() + i);
            y_p.erase(y_p.begin() + i);
            int N_p = x_p.size();
            for (int j=0; j<N_p; j++) {
                vector<int> x_pp = x_p;
                vector<int> y_pp = y_p;
                x_pp.erase(x_pp.begin() + j);
                y_pp.erase(y_pp.begin() + j);
                min_area = min(min_area, area(x_pp, y_pp));
            }
        }
        return min_area;
    }
    long long area(vector<int> x, vector<int> y) {
        sort(x.begin(), x.end());
        sort(y.begin(), y.end());
        long long x_length = *(x.end() - 1) - *(x.begin());
        long long y_length = *(y.end() - 1) - *(y.begin());
        long long side = max(abs(x_length), abs(y_length)) + 2;
        return side * side;
    }
};

int main() {
    vector<int> x = vector<int>();
    vector<int> y = vector<int>();

    x.push_back(1000000000);
    x.push_back(-1000000000);
    x.push_back(1000000000);
    x.push_back(-1000000000);

    y.push_back(1000000000);
    y.push_back(1000000000);
    y.push_back(-1000000000);
    y.push_back(-1000000000);

    MinimumSquareEasy ___test;
    printf("%lld\n", ___test.minArea(x, y));
}
