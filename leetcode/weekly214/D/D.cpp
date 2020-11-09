#include <bits/stdc++.h>
using namespace std;

constexpr int MODULUS = 1000000007;
template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}

struct BIT {
	vector<long long> s;
	BIT(int n) : s(n) {}
	void pointSet(int pos, long long dif) { // a[pos] += dif
		for (; pos < s.size(); pos |= pos + 1) s[pos] += dif;
	}
	long long rangeSum(int pos) { // sum of values in [0, pos)
		long long res = 0;
		for (; pos > 0; pos &= pos - 1) res += s[pos-1];
		return res;
	}
};


class Solution {
public:

    int createSortedArray(vector<int>& instructions) {

        auto u = vector<int>(instructions);
        sort_unique(u);

        vector<int> indexOf[100009];

        for (int i=0; i<instructions.size(); i++) {
            auto e = instructions[i];
            indexOf[e].push_back(i);
        }

        for (auto e : u) {
            reverse(indexOf[e].begin(), indexOf[e].end());
        }

        auto s = BIT(instructions.size() + 100);

        int ret = 0;

        for (auto e : u) {
            int count = indexOf[e].size();
            for (auto i : indexOf[e]) {
                auto leftCost = s.rangeSum(i);
                auto rightCost = i + 1 - leftCost - count;
                auto cost = min(leftCost, rightCost);
                ret += (cost % MODULUS);
                ret %= MODULUS;
                count--;
            }

            for (auto i : indexOf[e]) {
                s.pointSet(i, 1);
            }
        }

        return ret;

    }
};

int main() {

    auto s = Solution();
    auto instructions = vector<int>(100000, 7);
    cout << "ret=" << s.createSortedArray(instructions) << endl;

}