using namespace std;
#include <bits/stdc++.h>

int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int tt = 1;
	cin >> tt;
	while(tt--){
		int n,k;
		cin >> n >> k;
		vector<int> a(n),b(n);
		for(int i = 0; i < n; i++){
			cin >> a[i];
		}
		for(int i = 0; i < n; i++){
			cin >> b[i];
		}
		const int N = 1 + max(accumulate(a.begin(),a.end(),0),accumulate(b.begin(),b.end(),0));

		if(k == n){
			cout << (min(accumulate(a.begin(),a.end(),0),accumulate(b.begin(),b.end(),0))) << '\n';
			continue;
		}
		long long int dp[N][N];
		memset(dp,0,sizeof(dp));
		dp[0][0] = (1ll << (k+1)) - 1;
		for(int i = 0; i < n; i++){
			for(int x = N-1; x >= a[i]; x--){
				for(int y = N-1;y >= b[i];y--){
					dp[x][y] |= dp[x-a[i]][y-b[i]] << 1;
				}
			}
		}
		int ans = 0;
		for(int i = N-1; i >= 0; i--){
			if(i <= ans)break;
			for(int j = N-1; j >= 0; j--){
				if(j <= ans)break;
				if(dp[i][j] >> k & 1){
					ans = min(i,j);
				}
			}
		}
		cout << (ans) << '\n';
	}
	return (0-0);
}