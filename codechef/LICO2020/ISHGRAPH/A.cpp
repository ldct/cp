#include <bits/stdc++.h>

using namespace std;

constexpr size_t MAX_COORD = 2e6 + 5;

int x_sum[MAX_COORD];
int y_sum[MAX_COORD];

int main() {
  
  int N;

  cin >> N;

  for (int i=0; i<MAX_COORD; i++) {
    x_sum[i] = 0;
    y_sum[i] = 0;
  }

  for (int i=0; i<N; i++) {
    int x0, x1, x2;
    int y0, y1, y2;

    cin >> x0 >> y0 >> x1 >> y1 >> x2 >> y2;

    int maxX, maxY, minX, minY;

    maxX = max(x0, max(x1, x2));
    minX = min(x0, min(x1, x2));
    maxY = max(y0, max(y1, y2));
    minY = min(y0, min(y1, y2));

    x_sum[2*minX+1] += 1;
    x_sum[2*maxX-1] -= 1;

    y_sum[2*minY+1] += 1;
    y_sum[2*maxY-1] -= 1;
  }

  for (int i=1; i<MAX_COORD; i++) {
    x_sum[i] += x_sum[i-1];
    y_sum[i] += y_sum[i-1];
  }

  int M;
  cin >> M;

  for (int i=0; i<M; i++) {

    string s;
    cin >> s;

    bool is_x;
    if (s == "x") {
      is_x = true;
    } else if (s == "y") {
      is_x = false;
    } else {
      assert(false);
    }
    cin >> s; // equal sign
    int c; 
    cin >> c;

    // cout << (is_x ? "x" : "y") << "=" << c;
    if (is_x) {
      cout << x_sum[2*c];
    } else {
      cout << y_sum[2*c];
    }
    cout << endl;


  }

  return 0;
}
