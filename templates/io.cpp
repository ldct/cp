template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }
template<class T> ostream& operator << (ostream& os, const set<T>& v) { os << "{"; for (const T& e : v) os << e << ", "; return os << "}"; }

/*
template<class T1, class T2>
ostream& operator << (ostream& os, const pair<T1,T2>& v) {
    return os << "(" << v.first << ", " << v.second << ")";
}
*/

/*
template<class T>
ostream& operator << (ostream& os, const vector<T>& v) {
    os << "[";
    for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; }
    return os << "]";
}
*/

/*
template<class T>
ostream& operator << (ostream& os, const set<T>& v) {
    os << "{";
    for (const T& e : v) {
        os << e << ", ";
    }
    os << "}";
}
*/

/*
vector<int> py_slice(vector<int>& v, int skip) {
  vector<int> ret;
  for (int i=0; i<v.size(); i+=skip) ret.push_back(v[i]);
  return ret;
}
*/