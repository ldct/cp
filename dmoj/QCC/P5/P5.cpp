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

double INF;

void dijkstra(int s, const vector<vector<pair<int, double>>> & adj, vector<double> & d) {
    int n = adj.size();
    d.assign(n, INF);

    d[s] = 0;
    using pdi = pair<double, int>;
    priority_queue<pdi, vector<pdi>, greater<pdi>> q;
    q.push({0.0, s});
    while (!q.empty()) {
        int v = q.top().second;
        double d_v = q.top().first;
        q.pop();
        if (d_v != d[v])
            continue;

        for (auto edge : adj[v]) {
            int to = edge.first;
            double len = edge.second;

            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                q.push({d[to], to});
            }
        }
    }
}

int N, M, K;
double R, T;

vector<double> X;
vector<double> Y;
vector<double> Z;

double sqr(double x) { return x*x; }

double gsd(double x_A, double y_A, double z_A, double x_B, double y_B, double z_B) {
  double dist = sqrt(sqr(x_B-x_A)+sqr(y_B-y_A)+sqr(z_B-z_A));
  double phi = asin(dist / (2*R));
  return 2*phi*R;
}

double gsd(int a, int b) {
  return gsd(X[a], Y[a], Z[a], X[b], Y[b], Z[b]);
}

vector<int> airports;
vector<int> cases;


int main() {

  cin >> N >> M >> R >> T >> K;

  INF = 10000*R;

  for (int k=0; k<K; k++) {
    int a;
    cin >> a;
    airports.push_back(a-1);
  }

  for (int i=0; i<N; i++) {
    int v;
    double x, y, z;
    cin >> v >> x >> y >> z;
    cases.push_back(v);
    X.push_back(x); Y.push_back(y); Z.push_back(z);
  }

  vector<vector<pair<int, double>>> adj1;

  for (int i=0; i<=N; i++) adj1.push_back({});

  for (int i=0; i<M; i++) {
    int u, v;
    cin >> u >> v;
    u--; v--;
    adj1[u].push_back({v, gsd(u, v)});
    adj1[v].push_back({u, gsd(v, u)});
  }

  vector<double> dist0, dist_bye;

  dijkstra(0, adj1, dist0);

  for (const auto a : airports) {
    adj1[N].push_back({a, 0.0});
  }

  dijkstra(N, adj1, dist_bye);

  int ret = -1;

  for (int i=0; i<N; i++) {
    // cout << cases[i] << " " << dist0[i] + dist_bye[i] << endl;
    if (dist0[i] + dist_bye[i] < double(T)) ret = max(ret, cases[i]);
  }

  cout << ret << endl;

  return 0;
}
