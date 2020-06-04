#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int>> edges;
vector<pair<int, pair<int, int>>> ordered_edges;

vector<pair<int, int>> order;
vector<int> degree;

int N, M;

void ans() {

  vector<int> ret;
  int i=0;
  int j=0;

  int first = 0;
  while (i < order.size()) {
    if (!order[i].first == first + 1) {
      printf("-1\n");
      return;
    }
    first = order[i].first;
    // printf("considering all node with topic %d\n", first);
    while (i < order.size() && order[i].first == first) {
      auto node = order[i].second;
      ret.push_back(node);
      // printf("node: %d\n", node);
      if (degree[node] != first - 1) {
        printf("-1\n");
        return;
      }
      i += 1;


      while (j < ordered_edges.size() && ordered_edges[j].first == first && ordered_edges[j].second.first == node) {
        auto a = ordered_edges[j].second.first;
        auto b = ordered_edges[j].second.second;

        degree[b] += 1;

        // printf("edge: (%d, %d)\n", a, b);
        j += 1;
      }


    }
  }

  if (!(i == order.size())) {
    malloc(1000000000000000);
  }

  if (!(j == ordered_edges.size())) {
    malloc(1000000000000000);
  }


  for (int i=0; i<ret.size(); i++) {
    printf("%d ", ret[i]);
  }
  printf("\n");

}

int main() {  
  scanf("%d %d\n", &N, &M);

  for (int i=0; i<M; i++) {
    int a, b;
    scanf("%d %d\n", &a, &b);
    edges.push_back(make_pair(a, b));
  } 

  degree.push_back(0);
  for (int i=1; i<=N; i++) {
    degree.push_back(0);
    int t;
    scanf("%d", &t);

    order.push_back(make_pair(t, i));
  }

  for (int i=0; i<edges.size(); i++) {
    auto p = edges[i];
    auto a = p.first;
    auto b = p.second;

    ordered_edges.push_back(make_pair(order[a-1].first, make_pair(a, b)));
    ordered_edges.push_back(make_pair(order[b-1].first, make_pair(b, a)));
  }

  sort(order.begin(), order.end());
  sort(ordered_edges.begin(), ordered_edges.end());

  ans();

  return 0;
}
