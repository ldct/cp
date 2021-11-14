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

class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
      //  = 0;
      sort(tasks.rbegin(), tasks.rend());
      cout << tasks << endl;
      multiset<int> tree(workers.begin(), workers.end());
      int ret = 0;
      for (int i=0; i<tasks.size(); i++) {
        if (tree.size() == 0) break;
        if (pills == 0) {
          if (*tree.rbegin() >= tasks[i]) {
            cout << "no match " << tasks[i] << endl;
            ret += 1;
            tree.erase(next(tree.rbegin()).base());
          }
        } else {
          auto it = tree.lower_bound(tasks[i] - strength);
          if (it != tree.end()) {
            cout << "match w pill " << tasks[i] << endl;
            tree.erase(it);
            pills--;
            ret++;
          } else {
            cout << "no match 2 " << tasks[i] << endl;
          }
        }
      }
      return ret;
    }
};

int main() {

  auto s = Solution();
  vector<int> tasks = {3,2,1};
  vector<int> workers = {0,3,3};
  cout << s.maxTaskAssign(tasks, workers, 1, 1) << endl;

  return 0;
}
