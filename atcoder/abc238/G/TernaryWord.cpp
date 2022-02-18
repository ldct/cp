#include <bits/stdc++.h>
using namespace std;
#define endl '\n'
#define int long long
#define i32 int32_t
#define i64 int64_t

namespace io_aux {
  template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
  template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
  template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  template<class T> ostream& operator << (ostream& os, const multiset<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }
  namespace aux {
    template<size_t...> struct seq{}; template<size_t N, size_t... I> struct gs : gs<N-1, N-1, I...>{}; template<size_t... I> struct gs<0, I...> : seq<I...>{}; template<class C, class T, class U, size_t... I> void pt(basic_ostream<C,T>& os, U const& t, seq<I...>){ using w = int[]; (void)w{0, (void(os << (I == 0? "" : ", ") << get<I>(t)), 0)...};} }
  template<class C, class T, class... A> auto operator<<(basic_ostream<C, T>& os, tuple<A...> const& t) -> basic_ostream<C, T>& { os << "("; aux::pt(os, t, aux::gs<sizeof...(A)>()); return os << ")"; }
} using namespace io_aux;

void setBit(i64& a, int i) {
  a |= (1LL << i);
}

struct TernaryWord {
  /*the binary-coded representation
  00 -> 0
  01 -> 1
  10 -> 2

  in unnormalized form,
  11 -> 0
  */
  i64 bct;

  TernaryWord(i64 _bct) : bct(_bct) {}

  vector<int> as_vec() {
    vector<int> ret;
    for (int i=0; i<32; i++) {
      int b = bct & (1LL << (2*i));
      int a = bct & (1LL << (2*i+1));

      if (!a && !b) {
        ret.push_back(0);
      } else if (!a && b) {
        ret.push_back(1);
      } else if (a && !b) {
        ret.push_back(2);
      } else {
        ret.push_back(3);
        // assert(false);
      }
    }
    reverse(ret.begin(), ret.end());
    return ret;
  }

  TernaryWord(vector<int> vec) {
    while (vec.size() != 32) {
      vec.push_back(0);
    }
    reverse(vec.begin(), vec.end());

    bct = 0;

    for (int i=0; i<vec.size(); i++) {
      auto a = vec[i];
      if (a == 0) {
        // pass
      } else if (a == 1) {
        setBit(bct, 2*i);
      } else {
        assert(a == 2);
        setBit(bct, 2*i + 1);
      }
    }
  }

  static TernaryWord random() {
    vector<int> ret;
    while (ret.size() != 28) {
      ret.push_back(rand() % 3);
    }
    while (ret.size() != 32) {
      ret.push_back(0);
    }
    reverse(ret.begin(), ret.end());

    return TernaryWord(ret);
  }

  TernaryWord normalize() {
    uint64_t odd_bits = (unsigned long long)bct & 0xAAAAAAAAAAAAAAAA;
    uint64_t even_bits = (unsigned long long)bct & 0x5555555555555555ULL;

    // cout << even_bits << endl;
    // cout << odd_bits << endl;

    odd_bits = odd_bits >> 1;

    // cout << even_bits << endl;
    // cout << odd_bits << endl;

    uint64_t new_odd = odd_bits & ~even_bits;
    uint64_t new_even = ~odd_bits & even_bits;

    new_odd = new_odd << 1;
    return TernaryWord(new_odd | new_even);
  }


};


i32 main() {

  for (int i=0; i<1; i++) {
    auto tw1 = TernaryWord::random();
    auto tw2 = TernaryWord::random();

    auto v1 = tw1.as_vec();
    auto v2 = tw2.as_vec();

    for (int i=0; i<v1.size(); i++) {
      v1[i] += v2[i];
      v1[i] %= 3;
    }

    cout << tw1.as_vec() << endl;
    cout << tw2.as_vec() << endl;
    cout << v1 << endl;
    cout << TernaryWord((tw1 ^ tw2).bct).as_vec() << endl;
  }

  return 0;
}

// DO NOT USE FOR INTERACTIVE PROBLEMS