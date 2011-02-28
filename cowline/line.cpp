/*
PROG: line
LANG: C++
ID: xuanji2
*/

#define VIEW(x) printf("viewing %s=", #x);int vx;for(vx=0;vx<x.size();vx++)printf("%d",x[vx]);

#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <math.h>

int fact(int n) {
    return (n == 0) ? 1 : (n * fact(n-1));
}

int indexof(std::vector<int> v, int elem) {
    int i=0;
    for (i=0;i<v.size();i++) {
        if (v[i] == elem)
            return i;
    }
}

int which(std::vector<int> p) {
    if (p.size() == 1)
        return 1;
    std::vector<int> ps = std::vector<int>(p);
    std::sort(ps.begin(), ps.end());
    int pn = p[0];
    p.erase(p.begin());
    return (indexof(ps, pn) * fact(p.size())) + which(p);
}

void print(std::vector<int> p, int N, int n) {
    if (p.size() == 1) {
        printf("%d ", p[0]);
        return;
    } 
    std::sort(p.begin(), p.end());
    int idx = ceil((double)n/(double)(N-1));
    printf("%d ", p[idx-1]);
    p.erase(p.begin() + idx - 1);
    print(p, N-1, n - fact(N-1)*(idx-1));
}

int main() {

    FILE *fin  = fopen("line.in", "r");
    FILE *fout = fopen("line.out", "w");

    int N,K;
    int i;
    fscanf(fin, "%d %d\n", &N, &K);
    for (i=0; i < K; i++) {
        char pq;
        int j;
        fscanf(fin, "%c\n", &pq);
        if (pq == 'P') {
            int p;
            fscanf(fin, "%d\n", &p);
            std::vector<int> perm;
            for (j=0; j<N; j++) 
                perm.push_back(j+1);
            print(perm, N, p);
            printf("\n");
        }
        if (pq == 'Q') {
            std::vector<int> perm;
            for (j=0; j<N; j++) {
                int n;
                fscanf(fin, "%d", &n);
                perm.push_back(n);
            }
            fscanf(fin, "\n");
            printf("%d\n", which(perm));
        }
    }
    
    return 0;
}
