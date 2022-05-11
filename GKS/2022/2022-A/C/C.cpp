#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

int T, N;
string S;
bool has_contradiction;

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

void force_char(int i, int j, Eq2SAT& engine) {
  cout << S[i] << S[j] << endl;
  if (S[i] == '?' && S[j] == '?') {
    if (!engine.neq(i, j)) has_contradiction = true;
  } else if (S[i] != '?' && S[j] != '?') {
    if (S[i] == S[j]) has_contradiction = true;
  } else if (S[i] == '0') {
    if (!engine.eq(N+1, j)) has_contradiction = true;
  } else if (S[i] == '1') {
    if (!engine.eq(N+2, j)) has_contradiction = true;
  } else if (S[j] == '0') {
    if (!engine.eq(N+1, i)) has_contradiction = true;
  } else if (S[j] == '1') {
    if (!engine.eq(N+2, i)) has_contradiction = true;
  } else {
    assert(false);
  }
}

void force_ss(int i, int j, Eq2SAT& engine) {
  if (j >= S.size()) return;
  for (int p=i; p<j; p++) {
    int q = j-p-1;
    force_char(p, q, engine);
  }
}

void ans(int t) {
  auto engine = Eq2SAT(N+5);
  engine.neq(N+1, N+2);
  has_contradiction = false;

  for (int i=0; i<S.size(); i++) {
    force_ss(i, i+5, engine);
    force_ss(i, i+6, engine);
  }

  if (has_contradiction) {
      cout << "Case #" << (t) << ": IMPOSSIBLE" << endl;
  } else {
      cout << "Case #" << (t) << ": POSSIBLE" << endl;
  }

}

i32 main() {
  cin >> T;
  for (int t=1; t<=T; t++) {
    cin >> N >> S;
    ans(t);
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS