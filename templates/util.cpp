template<typename T> void sort_unique(vector<T>& v) { sort(v.begin(), v.end()); v.erase(unique(v.begin(), v.end()),v.end());}

/**
template<typename T> void sort_unique(vector<T>& v) {
  sort(v.begin(), v.end());
  v.erase(unique(v.begin(), v.end()),v.end());
}
**/