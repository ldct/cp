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

int K, Q, threshold;
string S;

class Node;
Node* lut[1 + (1<<19)];


class Node {
public:
  Node* parent = nullptr;
  unique_ptr<Node> lTree;
  unique_ptr<Node> rTree;

  int game_idx;
  char my_val;
  long long score;

  Node(string& a) : Node(a, a.size()-1) {}
  Node(string&a, int _game_idx) {

    game_idx = _game_idx;

    my_val = a[_game_idx];

    if (game_idx < threshold) {
    } else {

      int i = (1 << K) - 2 - game_idx;
      int b = 2*i+1;
      int c = 2*i+2;

      lTree = unique_ptr<Node>(new Node(a, (1 << K) - 2 - b));
      rTree = unique_ptr<Node>(new Node(a, (1 << K) - 2 - c));

      lTree->parent = this;
      rTree->parent = this;
    }
    recalc();
    lut[game_idx] = this;
  }
  void prop() {
    recalc();
    if (parent) parent->prop();
  }
  void recalc() {
    if (game_idx < threshold) {
      score = (my_val == '?' ? 2 : 1);
      return;
    }
    // cout << "recalc" << make_tuple(game_idx, my_val) << endl;
    score = 0;
    if (my_val == '?' || my_val == '0') score += rTree->score;
    if (my_val == '?' || my_val == '1') score += lTree->score;
  }
};

int main() {
  cin >> K;
  cin >> S;
  cin >> Q;

  threshold = 1 << (K-1);

  Node root(S);

  while (Q --> 0) {
    int a;
    char b;
    cin >> a >> b;
    a--;
    lut[a]->my_val = b;
    lut[a]->prop();
    cout << root.score << endl;
  }

  return 0;
}