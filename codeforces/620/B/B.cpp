#include <iostream>

using namespace std;

const int SEGMENTS[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
const int STRIDES[10] = {
	2383366,
	2650003,
	2950000,
	2949999,
	2850001,
	2950001,
	3049997,
	2750004,
	3149999
};

long sum(int a, int b) {
	long ret = 0;

	while (1) {


		if (a == b+1) return ret;

		if (a % 100000 == 1 && a + 100000 <= b) {
			int s = (a-1)/100000;
			ret += STRIDES[s];
			a += 100000;
			continue;
		}

		string s = to_string(a);
		for (int j=0; j<s.size(); j++) {
			char c = s[j];
			ret += SEGMENTS[c - '0'];
		}
		a++;
	}
}

int main () {

	int a, b;

	cin >> a >> b;

	cout << sum(a, b) << endl;
	
}