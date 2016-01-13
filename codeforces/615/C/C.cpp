#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
#include <cassert>
#include <map>

using namespace std;

set<string> substrings;

string S, T;

map<string, pair<int, string>> memo;

pair<int, string> minCoatings(string s) {
	// minimum-cost way to assemble T[start:] from substrings

	if (memo.find(s) != memo.end()) {
		return memo[s];
	}

	if (substrings.find(s) != substrings.end()) {
		return make_pair(1, s);
	} else {
		int retNum = 1000000;
		string retStr = string("");

		for (int i=1; i<s.size(); i++) {
			string head = s.substr(0, i);
			string tail = s.substr(i);

			if (substrings.find(head) != substrings.end()) {
				auto candidate = minCoatings(tail);
				if (candidate.first != -1) {
					if (1+candidate.first < retNum) {
						retNum = 1+candidate.first;
						retStr = head;
					}
				}
			}
		}



		if (retStr.size() == 0) {
			memo[s] = make_pair(-1, retStr);
		} else {
			memo[s] = make_pair(retNum, retStr);			
		}
		return memo[s];

	}

}

pair<int, int> whereDidThisComeFrom(string s) {
	if (S.find(s) != -1) {
		return make_pair(S.find(s) + 1, S.find(s) + s.size());
	} else {
		reverse(s.begin(), s.end());
		return make_pair(S.find(s) + s.size(), S.find(s) + 1);
	}
}

int main () {
	cin >> S >> T;

	for (int i=0; i<S.size(); i++) {
		for (int j=1; j<=S.size()-i; j++) {
			substrings.insert(S.substr(i, j));
		}
	}

	cout << "done a" << endl;

	reverse(S.begin(), S.end());

	for (int i=0; i<S.size(); i++) {
		for (int j=1; j<=S.size()-i; j++) {
			substrings.insert(S.substr(i, j));
		}
	}

	cout << "done b" << endl;

	cout << "substrings.size: " << substrings.size() << endl;

	reverse(S.begin(), S.end());

	auto res = minCoatings(T);

	cout << "memo.size: " << memo.size() << endl;

	cout << "done c" << endl;

	vector<string> parts;

	cout << res.first << endl;

	if (res.first == -1) {
		return 0;
	}

	string remainingString = T;

	while (res.first > 1) {		
		parts.push_back(res.second);
		remainingString = remainingString.substr(res.second.size());
		res = minCoatings(remainingString);
	}
	assert(res.first == 1);
	parts.push_back(res.second);

	cout << "done d" << endl;

	for (int i=0; i<parts.size(); i++) {
		pair<int, int> where = whereDidThisComeFrom(parts[i]);
		cout << where.first << " " << where.second << endl;
	}

}