#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool has_cycle;
    int N;
    int M;
    bool visited[509][509];
    vector<vector<char>> grid;
    
    void dfs(char c, int sx, int sy, int spx, int spy) {
        // cout << "dfs" << endl;
        vector<pair<pair<int, int>, pair<int, int>>> stack;

        stack.push_back({{sx, sy}, {spx, spy}});

        while (stack.size()) {
            auto pp = stack[stack.size() - 1];
            stack.pop_back();
            int x = pp.first.first;
            int y = pp.first.second;
            int px = pp.second.first;
            int py = pp.second.second;

            // cout << "dfs " << x << " " << y << " " << px << " " << py << endl;

            visited[x][y] = true;

            const vector<pair<int, int>> directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};


            for (int i=0; i<4; i++) {
                pair<int, int> p = directions[i];
                int new_x = x + p.first;
                int new_y = y + p.second;
                if (new_x == px && new_y == py) continue;
                if (!(0 <= new_x && new_x < N)) continue;
                if (!(0 <= new_y && new_y < M)) continue;
                if (grid[new_x][new_y] != c) continue;
                
                if (visited[new_x][new_y]) {
                    // cout << "cycle " << x << " " << y << " " << new_x << " " << new_y << endl;
                    has_cycle = true;
                    return;
                }

                stack.push_back({{new_x, new_y}, {x, y}});
            }

        }
    }

    bool containsCycle(vector<vector<char>>& _grid) {
        grid = _grid;
        has_cycle = false;
        N = grid.size();
        M = grid[0].size();


        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                visited[i][j] = false;
            }
        }

        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (!visited[i][j]) {
                    dfs(grid[i][j], i, j, i, j);
                    if (has_cycle) return true;
                }
            }
        }
        return has_cycle;
    }
};

int main() {
    int N = 500;
    int M = 500;

    vector<vector<char>> grid = {{'a', 'b', 'b'}, {'b', 'z', 'b'}, {'b', 'b', 'a'}};

    // for (int i=0; i<N; i++) {
    //     vector<char> row;
    //     for (int j=0; j<M; j++) {
    //         row.push_back('a');
    //     }
    //     grid.push_back(row);
    // }

    Solution s;

    cout << s.containsCycle(grid) << endl;
    cout << s.containsCycle(grid) << endl;


    return 0;
}