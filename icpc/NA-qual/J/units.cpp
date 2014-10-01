#include <cstdio>
#include <utility>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

typedef pair<string, string> ss;
typedef pair<ss, int> link;

map<string, vector<link> > partition_lhs(vector<link> links) {
  map<string, vector<link> > ret;

  for (int i=0; i<links.size(); i++) {
    //a = n b

    string a = links[i].first.first;
    string b = links[i].first.second;
    int n = links[i].second;

    ret[a].push_back(links[i]);

  }

  return ret;

}

vector<link> eliminate(vector<link> links, int row) {
  //a = n b

  string a = links[row].first.first;
  string b = links[row].first.second;
  int n = links[row].second;

  for (int i=0; i<links.size(); i++) {
    // c = m d

    string c = links[i].first.first;
    string d = links[i].first.second;
    int m = links[i].second;

    if (d == a) {
      links[i].second = n * m;
      links[i].first.second = b;
    }

  }
  return links;

}

vector<link> relax(vector<link> links) {
  int largest_factor = 0;
  string largest_RHS;

  for (int i=0; i<links.size(); i++) {
    if (links[i].second > largest_factor) {
      largest_factor = links[i].second;
      largest_RHS = links[i].first.second;
    }
  }

  for (int i=0; i<links.size(); i++) {
    //a = n b

    string b = links[i].first.second;
    int n = links[i].second;

    if (b == largest_RHS) {
      continue;
    }

    links[i].first.first = b;
    links[i].first.second = largest_RHS;
    links[i].second = largest_factor / n;

  }

  return links;
}

int main() {

  int N;

  while (1) {
    scanf("%d", &N);
    // printf("%d\n", N);

    if (N == 0) {
      return 0;
    }

    set<string> units;
    vector<link> links;

    for (int i=0; i<N; i++) {
      char u[100];
      scanf("%s", u);
      units.insert(string(u));
    }

    for (int i=0; i<N-1; i++) {
      char a[100];
      int b;
      char c[100];

      scanf("%s = %d %s", a, &b, c);

      ss my_ss = make_pair(string(a), string(c));

      links.push_back(make_pair(my_ss, b));
    }

    for (int k=0; k<links.size(); k++) {
      for (int i=0; i<links.size() + 2; i++) {
        for (int j=0; j<links.size(); j++) {
          links = eliminate(links, j);
        }
      }
      map<string, vector<link> > part_lhs = partition_lhs(links);
      links.clear();
      for(map<string, vector<link> >::iterator it = part_lhs.begin(); it!=part_lhs.end(); it++) {
        vector<link> relaxed;
        if (it->second.size() > 1) {
          relaxed = relax(it->second);
        } else {
          relaxed = it->second;
        }
        for (int i=0; i<relaxed.size(); i++) {
          links.push_back(relaxed[i]);
        }
      }
    }


    vector<pair<int, link > > ordered_links;


    //print
    for (int i=0; i<links.size(); i++) {
      string a = links[i].first.first;
      string b = links[i].first.second;
      int n = links[i].second;

      ordered_links.push_back(make_pair(n, links[i]));

    }

    sort(ordered_links.begin(), ordered_links.end());

    //print

    int large = ordered_links[ordered_links.size() - 1].second.second;

    for (int i=ordered_links.size() - 1; i>=0; i--) {
      string a = ordered_links[i].second.first.first;
      string b = ordered_links[i].second.first.second;
      int n = ordered_links[i].second.second;

      cout << large / n << a << " = ";
    }

    cout << large << ordered_links[0].second.first.second << endl;

  }

  return 0;
}
