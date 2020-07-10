template<class T1, class T2> ostream& operator << (ostream& os, const pair<T1,T2>& v) { return os << "(" << v.first << ", " << v.second << ")"; }
template<class T> ostream& operator << (ostream& os, const vector<T>& v) { os << "["; for (int i=0; i<v.size(); i++) { os << v[i]; if (i < v.size() - 1) os << ", "; } return os << "]"; }

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