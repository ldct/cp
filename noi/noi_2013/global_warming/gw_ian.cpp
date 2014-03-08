#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;
int n, a, b, c, p = -1, v = -1, numIsland = 0, curNumIsland = 0;
priority_queue <int> peak, valley;
int main(){
    scanf("%d", &n);
    scanf("%d %d %d", &a, &b, &c);
    if(a > b)
        peak.push(a);
    if(b > a && b > c)
        peak.push(b);
    else if(b < a && b < c)
        valley.push(b);
    else if(b > a && b == c)
        p = c;
    else if(b < a && b == c)
        v = c;
    for(int i = 2; i < n - 1; i++){
        a = b;
        b = c;
        scanf("%d", &c);
        if(b > a && b > c)
            peak.push(b);
        else if(b < a && b < c)
            valley.push(b);
        else if(b > a && b == c)
            p = c;
        else if(b < a && b == c)
            v = c;
        else if(b == a && b > c && p == b)
            peak.push(b);
        else if(b <= a && b < c && v == b)
            valley.push(b);
        if(p != b)
            p = -1;
        if(v != b)
            v = -1;
    }
    if(c > b || (c == b && p == b))
        peak.push(c);
    while(!peak.empty() || !valley.empty()){
        //printf("%d %d, ", peak.top(), valley.top());
        if(valley.empty())
            break;
        else if(!peak.empty() && peak.top() > valley.top()){ //if peak.top() == valley.top(), valley.top() calculated first
            curNumIsland++;
            peak.pop();
        }
        else{
            curNumIsland--;
            valley.pop();
        }
        numIsland = max(numIsland, curNumIsland);
    }
    if (numIsland == 0) //flat
        numIsland = 1;
    printf("%d", numIsland);
}