#include <vector>
#include <iostream>

using namespace std;

bool isSubsetSum(vector<int> items, int sum) {
	int n = items.size();
    bool subset[n + 1][sum + 1];

    for (int i = 0; i <= n; i++)
        subset[i][0] = true;

    for (int i = 1; i <= sum; i++)
        subset[0][i] = false;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= sum; j++) {
            if (j < items[i - 1])
                subset[i][j] = subset[i - 1][j];
            if (j >= items[i - 1])
                subset[i][j] = subset[i - 1][j]
                               || subset[i - 1][j - items[i - 1]];
        }
    }

    return subset[n][sum];
}

bool isKSubsetSum(vector<int> items, int target, int K) {
	vector<int> bigItems;
	for (const int item : items) {
		for (int i=0; i<K; i++) {
			bigItems.push_back(item);
		}
	}
	return isSubsetSum(bigItems, target);
}


int sushi(int N, int B, vector<int> A) {

	if (N == 1) {
		int sushiCost = A[0];
		if (B % sushiCost != 0) return -1;
		return B / sushiCost;
	}

	int low = 0;
	int high = B;
	int mid;

	if (!isKSubsetSum(A, B, high)) return -1;

	while (high - low > 2) {
		mid = (low + high) / 2;
		if (isKSubsetSum(A, B, mid)) {
			high = mid;
		} else {
			low = mid;
		}
	}

	for (int k=low; k<=B; k++) {
		if (isKSubsetSum(A, B, k)) return k;
	}

	return -1;
}
