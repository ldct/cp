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

int numFinds = 0;

pair<int, string> minCoatings(string s) {
	// minimum-cost way to assemble T[start:] from substrings

	if (memo.find(s) != memo.end()) {
		return memo[s];
	}

	numFinds++;
	if (substrings.find(s) != substrings.end()) {
		return make_pair(1, s);
	} else {

		for (int i=s.size(); i > 0; i--) {

			string head = s.substr(0, i);
			string tail = s.substr(i);

			numFinds++;
			if (substrings.find(head) == substrings.end()) continue;

			auto candidate = minCoatings(tail);

			if (candidate.first == -1) continue;

			memo[s] = make_pair(1+candidate.first, head);
			return memo[s];

		}

		memo[s] = make_pair(-1, "");
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

	cout << "done c, numFinds=" << numFinds << endl;

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