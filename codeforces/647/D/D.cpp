#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_N = 500000;

vector<pair<int, int>> edges;
vector<int> neighbours[MAX_N];
vector<int> nodes[MAX_N]; 
int degree[MAX_N];

int N, M;

void ans() {

  vector<int> ret;

  for (int topic=1; topic<=N; topic++) {
    // printf("checking topic %d\n", topic);
    for (auto node : nodes[topic]) {
      ret.push_back(node);
      // printf("  degree(%d)=%d\n", node, degree[node]);
      if (degree[node] != topic-1) {
        printf("-1\n");
        return;
      }
      for (auto neighbour : neighbours[node]) {
        if (degree[neighbour] == topic-1) {
          degree[neighbour] = topic;
        }
      }
    }
  }

  for (auto node : ret) {
    printf("%d ", node);
  }
  printf("\n");
}

int main() {  
  scanf("%d %d\n", &N, &M);

  for (int i=1; i<=N; i++) {
    degree[i] = 0;
  }

  for (int i=0; i<M; i++) {
    int a, b;
    scanf("%d %d\n", &a, &b);
    neighbours[a].push_back(b);
    neighbours[b].push_back(a);
  } 

  for (int i=1; i<=N; i++) {
    int t;
    scanf("%d", &t);

    nodes[t].push_back(i);
  }

  ans();

  return 0;
}
