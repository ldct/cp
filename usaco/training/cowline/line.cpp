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

FILE *fin;
FILE *fout;

long long fact(int n) {
    return (n == 0) ? 1 : (n * fact(n-1));
}

int indexof(std::vector<int> v, int elem) {
    int i=0;
    for (i=0;i<v.size();i++) {
        if (v[i] == elem)
            return i;
    }
}

long long which(std::vector<int> p) {
    if (p.size() == 1)
        return 1;
    std::vector<int> ps = std::vector<int>(p);
    std::sort(ps.begin(), ps.end());
    int pn = p[0];
    p.erase(p.begin());
    return (indexof(ps, pn) * fact(p.size())) + which(p);
}

void print(std::vector<int> p, long long n) { //long long ok, long not ok
    int N = (int) p.size();
    if (p.size() == 1) {
        fprintf(fout, "%d", p[0]);
        return;
    }
    std::sort(p.begin(), p.end());
    int idx = (int) ceil((double)n/(double)fact(N-1));
    fprintf(fout, "%d ", p[idx-1]);
    p.erase(p.begin() + idx - 1);
    print(p, n - fact(N-1)*(idx-1));
}

int main() {

    fin  = fopen("line.in", "r");
    fout = fopen("line.out", "w");

    int N,K;
    int i;
    fscanf(fin, "%d %d\n", &N, &K);
    for (i=0; i < K; i++) {
        char pq;
        int j;
        fscanf(fin, "%c\n", &pq);
        if (pq == 'P') {
            long long p;
            fscanf(fin, "%lld\n", &p);
            std::vector<int> perm;
            for (j=0; j<N; j++) 
                perm.push_back(j+1);
            print(perm, p);
            fprintf(fout, "\n");
        }
        if (pq == 'Q') {
            std::vector<int> perm;
            for (j=0; j<N; j++) {
                int n;
                fscanf(fin, "%d", &n);
                perm.push_back(n);
            }
            fscanf(fin, "\n");
            fprintf(fout, "%lld\n", which(perm));
        }
    }
    
    return 0;
}
