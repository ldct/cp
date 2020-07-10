#include <bits/stdc++.h>

using namespace std;

template<typename T>
class PQ_del { /* max priority queue with deletion */
public:
  priority_queue<T> pq;
  priority_queue<T> deleted;

  T top() { return pq.top(); }
  bool empty() { return pq.empty(); }
  bool size() { return pq.size() - deleted.size(); }
  void push(T e) { pq.push(e); }
  T pop() { return pq.pop(); }
  void remove(T e) {
    if (!pq.empty() && pq.top() == e) {
      pq.pop();
      while (!pq.empty() && !deleted.empty() && pq.top() == deleted.top()) {
        pq.pop();
        deleted.pop();
      }
    } else {
      deleted.push(e);
    }
  }
};

int main() { 
  PQ_del<int> pq;

  pq.push(-5);
  pq.push(-2);
  pq.push(-3);
  cout << pq.top() << endl;
  pq.remove(-3);
  pq.push(-1);
  pq.remove(-2);
  pq.push(-3);
  pq.remove(-1);
  cout << pq.top() << endl;
}
