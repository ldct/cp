#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t

// https://discuss.codechef.com/t/paritree-editorial/12277

constexpr int MODULUS = 1000000007;

long long modexp(long long b, long long e) {
	long long ans = 1;
	for (; e; b = b * b % MODULUS, e /= 2)
		if (e & 1) ans = ans * b % MODULUS;
	return ans;
}

struct Eq2SAT {
    vector<int> e;
    vector<int> enemy;
    Eq2SAT(int n) : e(n, -1), enemy(n, -1) {}
    int find(int x) {
        assert(x != -1);
        return e[x] < 0 ? x : e[x] = find(e[x]);
    }
    int merged_size() {
      // merge enemies
      for (int i=0; i<e.size(); i++) {
        int u = find(i);
        if (enemy[u] != -1) join(u, enemy[u]);
      }
      set<int> ret;
      for (int i=0; i<e.size(); i++) {
        int u = find(i);
        ret.insert(u);
      }
      return ret.size();
    }
    int join(int a, int b) {
        if (a == -1) return b;
        if (b == -1) return a;
        a = find(a), b = find(b);
        if (a == b) return a;
        if (e[a] > e[b]) swap(a, b);
        e[a] += e[b]; e[b] = a;
        return a;
    }
    bool enemy_pair(int a, int b) {
        if (a == -1) assert(false);
        if (b == -1) assert(false);
        if (enemy[a] == b) {
            assert(enemy[b] == a);
            return true;
        }
        return false;
    }
    bool eq(int a, int b) {
        // returns: true iff no contradiction
        a = find(a), b = find(b);
        if (a == b) return true;
        if (enemy_pair(a, b)) {
            return false;
        }

        int e_all = join(enemy[a], enemy[b]);

        a = join(a, b);

        if (e_all != -1) enemy[e_all] = a;
        enemy[a] = e_all;
        return true;
    }

    bool is_eq(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return true;
        return false;
    }

    bool neq(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (enemy_pair(a, b)) {
            return true;
        }

        int s1 = join(a, enemy[b]);
        int s2 = join(enemy[a], b);
        enemy[s1] = s2;
        enemy[s2] = s1;

        return true;
    }

    bool is_neq(int a, int b) {
        a = find(a), b = find(b);
        if (a == b) return false;
        if (enemy_pair(a, b)) {
            return true;
        }
        return false;
    }
};

int T;
int N, Q;

i32 main() {

  cin >> T;
  while (T --> 0) {
    cin >> N >> Q;

    auto engine = Eq2SAT(N);

    for (int i=0; i<N-1; i++) {
      int u, v;
      cin >> u >> v;
      u--; v--;
    }

    bool has_contradiction = false;

    for (int i=0; i<Q; i++) {
      int u, v, x;
      cin >> u >> v >> x;
      u--; v--;

      if (u == v) {
        if (x == 0) continue;
        has_contradiction = true;
      }

      if (x == 0) {
        if (!engine.eq(u, v)) has_contradiction = true;
      } else {
        if (!engine.neq(u, v)) has_contradiction = true;
      }
    }

    if (has_contradiction) {
      cout << 0 << endl;
    } else {
      cout << modexp(2, engine.merged_size()-1) << endl;
    }

  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS