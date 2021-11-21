class LeftIndexingBinaryList {
public:
  set<int> indexes0, indexes1;
  vector<int> elems;
  LeftIndexingBinaryList(vector<int>& a) {
    elems = vector<int>(a.begin(), a.end());
    for (int i=0; i<elems.size(); i++) {
      if (elems[i] == 0) {
        indexes0.insert(i);
      } else if (elems[i] == 1) {
        indexes1.insert(i);
      } else {
        assert(false);
      }
    }
  }

  int find0(int start) {
    auto r = indexes0.lower_bound(start);
    if (r == indexes0.end()) return -1;
    return *r;
  }

  int find1(int start) {
    auto r = indexes1.lower_bound(start);
    if (r == indexes1.end()) return -1;
    return *r;
  }

  int find(int val, int start) {
    if (val == 0) return find0(start);
    if (val == 1) return find1(start);
    assert(false);
  }

  void swap(int i, int j) {
    if (elems[i] == elems[j]) return;
    if (elems[i] == 1) {
      indexes0.erase(j);
      indexes0.insert(i);
      indexes1.erase(i);
      indexes1.insert(j);
      elems[i] = 0; elems[j] = 1;
    } else {
      indexes0.erase(i);
      indexes0.insert(j);
      indexes1.erase(j);
      indexes1.insert(i);
      elems[i] = 1; elems[j] = 0;
    }
  }
};
