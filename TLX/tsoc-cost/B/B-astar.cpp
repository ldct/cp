#include <cstring>
#include <iostream>
#include <queue>
using namespace std;

const int MAXN = 505;

int N;
int grid[MAXN][MAXN];

int visitedCount;

int mx[4] = {1, 0, -1, 0};
int my[4] = {0, 1, 0, -1};
inline int h(int a, int b, int c, int d) {
    return c-a + d-b;
}

long long minPathSum() {
#define piii pair<long long, pair<int, int>>
#define v first
#define x second.first
#define y second.second

    priority_queue<piii, vector<piii>, greater<piii> > pq;
    pq.push({grid[0][0] + h(0, 0, N - 1, N - 1), {0, 0}});

    long long res[N][N];
    memset(res, -1, sizeof(res));

    res[0][0] = grid[0][0];

    // A*
    while(pq.size()) {
        piii t = pq.top(); pq.pop();
        
        if (res[t.x][t.y] != -1 
            && t.v - h(t.x, t.y, N - 1, N - 1) > res[t.x][t.y])
            continue;

        ++visitedCount;
        
        if (t.x == N - 1 && t.y == N - 1)
            return res[N-1][N-1];

        for (int i = 0; i < 4; ++i) {
            int new_x = t.x + mx[i];
            int new_y = t.y + my[i];
            if (new_x >= 0 && new_y >= 0 && new_x < N && new_y < N
                && (res[new_x][new_y] == -1
                || res[new_x][new_y] > res[t.x][t.y] + grid[new_x][new_y]
                    + h(new_x, new_y, N - 1, N - 1))) {
                res[new_x][new_y] = res[t.x][t.y] + grid[new_x][new_y];
                pq.push({res[new_x][new_y] + h(new_x, new_y, N - 1, N - 1), {new_x, new_y}});
            }
        }   
    }
    return res[N-1][N-1];

#undef piii
#undef v
#undef x
#undef y
}

int main() {
    cin >> N;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> grid[i][j];
        }
    }

    visitedCount = 0;
    cout << "Min path sum: " << minPathSum() << endl;
    cout << "Number of visited cells: " << visitedCount << endl;
    return 0;
}
