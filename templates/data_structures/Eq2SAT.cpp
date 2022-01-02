#include <bits/stdc++.h>
using namespace std;

/*
Process queries on N boolean variables:
- set x_a == x_b
- set x_a != x_b
tested on https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1099
*/
struct Eq2SAT {
    vector<int> e;
    vector<int> enemy;
    Eq2SAT(int n) : e(n, -1), enemy(n, -1) {}
    int find(int x) {
        assert(x != -1);
        return e[x] < 0 ? x : e[x] = find(e[x]);
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

int main() {
    int n;
    cin >> n;
    auto engine = Eq2SAT(n);

    while (1) {
        int c, x, y;
        cin >> c >> x >> y;
        if (c == 0 && x == 0 && y == 0) break;

        if (c == 1) {
            if(!engine.eq(x, y)) {
                cout << -1 << endl;
            }
        } else if (c ==2) {
            if(!engine.neq(x, y)) {
                cout << -1 << endl;
            }
        } else if (c == 3) {
            cout << (engine.is_eq(x, y) ? 1 : 0) << endl;
        } else if (c == 4) {
            cout << (engine.is_neq(x, y) ? 1 : 0) << endl;
        } else {
            assert(false);
        }
    }
    return 0;
}