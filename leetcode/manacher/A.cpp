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

constexpr int delta = 0;

struct ManacherBase{
private:
		static const int maxn=1e5+1;
        int r[maxn];
        char s[maxn];
        int mid,n,i;

public:
        ManacherBase():mid(0),i(0),n(1)
        {
        	memset(r,-1,sizeof(int)*maxn);
        	s[0]='$';
        	r[0]=0;
        }

        int get(int pos)
        {
        		pos++;
                if(pos<=mid)
                        return r[pos];
                else
                        return min(r[mid - (pos - mid)], n - pos - 1);
        }

        void addLetter(char c)
        {
                s[n]=s[n+1]=c;

                while(s[i - r[i] - 1 + delta] != s[i + r[i] + 1])
                        r[++i] = get(i-1);
                r[mid=i]++, n++;
        }

        int maxPal()
        {
                return ( n - mid - 1 ) * 2 + 1 - delta;
        }
} ;

class Solution {
public:

  vector<int> prefixes(string s) {
    vector<int> ret;

    ManacherBase m;
    int i=0;
    for (char c : s) {
      m.addLetter(c);
      ret.push_back(m.get(i++));
    }

    return ret;
  }

  long long maxProduct(string s) {


    vector<int> a = prefixes(s);

    cout << a << endl;

    reverse(s.begin(), s.end());
    vector<int> b = prefixes(s);
    reverse(b.begin(), b.end());

    for (int i=0; i<a.size(); i++) {
      int candidate = (2*a[i]-1)*(2*b[i]-1);
      cout << candidate << endl;
    }

    return 42;
  }
};

int main() {

  string s = "aaaaaaaaa";
  Solution sol;
  cout << sol.maxProduct(s) << endl;

  return 0;
}
