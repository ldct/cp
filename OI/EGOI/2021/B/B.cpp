#include <bits/stdc++.h>
using namespace std;

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

typedef struct _Query {
  int l, r, idx, ans;
} Query;

ostream& operator << (ostream& os, const Query& q) { return os << "(" << q.l << ", " << q.r << ", " << q.ans << ")"; }


bool cmp(Query x, Query y) { return x.r < y.r; }

void update(int idx, int val, int bit[], int n) {
  for (; idx <= n; idx += idx&-idx)
    bit[idx] += val;
}

int bit_query(int idx, int bit[], int n) {
    int sum = 0;
    for (; idx>0; idx-=idx&-idx)
        sum += bit[idx];
    return sum;
}

void answerQueries(vector<int> arr, vector<Query>& queries) {
    sort(queries.begin(), queries.end(), cmp);
    int MAX = *max_element(arr.begin(), arr.end()) + 1;
    int n = arr.size();
    int q = queries.size();

    // initialising bit array
    int bit[n+1];
    memset(bit, 0, sizeof(bit));

    // holds the rightmost index of any number
    // as numbers of a[i] are less than or equal to 10^6
    int last_visit[MAX];
    memset(last_visit, -1, sizeof(last_visit));

    // answer for each query
    int query_counter = 0;
    for (int i=0; i<n; i++)
    {
        // If last visit is not -1 update -1 at the
        // idx equal to last_visit[arr[i]]
        if (last_visit[arr[i]] !=-1)
            update (last_visit[arr[i]] + 1, -1, bit, n);

        // Setting last_visit[arr[i]] as i and updating
        // the bit array accordingly
        last_visit[arr[i]] = i;
        update(i + 1, 1, bit, n);

        // If i is equal to r of any query  store answer
        // for that query in ans[]
        while (query_counter < q && queries[query_counter].r == i) {
            auto a = bit_query(queries[query_counter].r + 1, bit, n)-bit_query(queries[query_counter].l, bit, n);
            queries[query_counter].ans = a;
            query_counter++;
        }
    }
}

int N;
vector<int> A;
int a;

int main() {

  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  cin >> N;
  for (int i=0; i<2*N; i++) {
    cin >> a;
    A.push_back(a);
  }

  vector<vector<int>> indexes(N+1);
  for (int i=0; i<A.size(); i++) {
    indexes[A[i]].push_back(i);
  }

  vector<Query> queries;
  int q = 0;
  for (int i=1; i<=N; i++) {
    int l = indexes[i][0];
    int r = indexes[i][1];
    if (l > r) swap(l, r);
    l += 1;
    r -= 1;
    if (!(l <= r)) continue;
    Query query;
    query.l = l; query.r = r; query.idx = q;
    queries.push_back(query);
    q++;
  }

  answerQueries(A, queries);

  long long swap = 0;
  for (const auto& query : queries) {
    auto num_elems = query.r - query.l + 1;
    auto r = num_elems - query.ans;
    long long s = query.ans - r;
    swap += s;
  }

  cout << (N + swap/2) << endl;
  return 0;
}
