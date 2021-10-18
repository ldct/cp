#include <bits/stdc++.h>
using namespace std;


// Class to represent a graph
class Graph {
    int V; // No. of vertices'

    // Pointer to an array containing
    // adjacency listsList
    list<int>* adj;

public:
    Graph(int V); // Constructor

    // Function to add an edge to graph
    void addEdge(int u, int v);

    // Function to print the required topological
    // sort of the given graph
    void topologicalSort();
};

// Constructor
Graph::Graph(int V)
{
    this->V = V;
    adj = new list<int>[V];
}

// Function to add an edge to the graph
void Graph::addEdge(int u, int v)
{
    adj[u].push_back(v);
}

// Function to print the required topological
// sort of the given graph
void Graph::topologicalSort()
{
    // Create a vector to store indegrees of all
    // the vertices
    // Initialize all indegrees to 0
    vector<int> in_degree(V, 0);

    // Traverse adjacency lists to fill indegrees of
    // vertices
    // This step takes O(V+E) time
    for (int u = 0; u < V; u++) {
        list<int>::iterator itr;
        for (itr = adj[u].begin(); itr != adj[u].end(); itr++)
            in_degree[*itr]++;
    }

    // Create a set and inserting all vertices with
    // indegree 0
    multiset<int> s;
    for (int i = 0; i < V; i++)
        if (in_degree[i] == 0)
            s.insert(i);

    // Initialize count of visited vertices
    int cnt = 0;

    // Create a vector to store result (A topological
    // ordering of the vertices)
    vector<int> top_order;

    // One by one erase vertices from setand insert
    // adjacents if indegree of adjacent becomes 0
    while (!s.empty()) {

        // Extract vertex with minimum number from multiset
        // and add it to topological order
        int u = *s.begin();
        s.erase(s.begin());
        top_order.push_back(u);

        // Iterate through all its neighbouring nodes
        // of erased node u and decrease their in-degree
        // by 1
        list<int>::iterator itr;
        for (itr = adj[u].begin(); itr != adj[u].end(); itr++)

            // If in-degree becomes zero, add it to queue
            if (--in_degree[*itr] == 0)
                s.insert(*itr);

        cnt++;
    }

    // Check if there was a cycle
    if (cnt != V) {
        cout << -1;
        return;
    }

    // Print topological order
    for (int i = 0; i < top_order.size(); i++)
        cout << top_order[i] + 1 << " ";
}

int N, M;

int main() {

  cin >> N >> M;

  Graph g(N);
  for (int i=0; i<M; i++) {
    int a, b;
    cin >> a >> b;
    a--; b--;
    g.addEdge(a, b);
  }

  g.topologicalSort();
  cout << endl;

  return 0;
}
