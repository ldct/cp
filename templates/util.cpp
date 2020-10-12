template<class T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}
template<class T, class U> T round_div(const T n, const U d) { return ((n < 0) ^ (d < 0)) ? ((n - d/2)/d) : ((n + d/2)/d); }
long long modexp(long long b, long long e) { long long ans = 1; for (; e; b = b * b % MODULUS, e /= 2) if (e & 1) ans = ans * b % MODULUS; return ans;}

/**
template<class T> void sort_unique(vector<T>& v) {
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()),v.end());
}
**/

/**
template<class T, class U>
T round_div(const T n, const U d) {
  return ((n < 0) ^ (d < 0)) ? ((n - d/2)/d) : ((n + d/2)/d);
}
**/

/**
long long modexp(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}
**/