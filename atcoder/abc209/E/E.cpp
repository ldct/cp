#include <bits/stdc++.h>
using namespace std;

int N;
constexpr size_t V = 52*52*52;

vector<int> adj[V];
vector<int> adj_rev[V];
bool winning[V];
bool losing[V];
bool visited[V];
int degree[V];

void dfs(int v) {
  // if (adj[v].size() || adj_rev[v].size()) cout << "dfs(" << v << ")" << endl;
  visited[v] = true;
  for (int u : adj_rev[v]) {
      if (!visited[u]) {
          if (losing[v])
              winning[u] = true;
          else if (--degree[u] == 0)
              losing[u] = true;
          else {
              continue;
          }
          dfs(u);
      }
  }
}

int sig(char q) {
  if ('a' <= q && q <= 'z') return q - 'a';
  if ('A' <= q && q <= 'Z') return 26 + q - 'A';
  assert(false); return -1;
}

int sig(char a, char b, char c) {
  return sig(c) + sig(b)*52 + sig(a)*52*52;
}

int main() {

  vector<int> seeds;
  vector<int> states;

  memset(winning, 0, sizeof(winning));
  memset(losing, 0, sizeof(losing));
  memset(degree, 0, sizeof(degree));
  memset(visited, 0, sizeof(visited));

  cin >> N;
  for (int i=0; i<N; i++) {
    string S;
    cin >> S;

    int w = S.size();
    int u = sig(S[0], S[1], S[2]);
    int v = sig(S[w-3], S[w-2], S[w-1]);

    states.push_back(v);

    // cout << "u=" << u << "v=" << v << endl;

    adj[u].push_back(v);
    adj_rev[v].push_back(u);
  }

  for (int i=0; i<52*52*52; i++) {
    degree[i] = adj[i].size();
    if (degree[i] == 0) {
      losing[i] = true;
      winning[i] = false;
      seeds.push_back(i);
    }
  }

  for (const auto i : seeds) {
    dfs(i);
  }

  for (auto s : states) {
    // cout << s << " ";
    if (!visited[s]) {
      cout << "Draw" << endl;
    } else if (winning[s]) {
      cout << "Aoki" << endl;
    } else if (losing[s]) {
      cout << "Takahashi" << endl;
    } else {
      assert(false);
      cout << "Draw" << endl;
    }
  }

  cout << sig('Z', 'Z', 'Z') << " " << V << endl;

  return 0;
}
