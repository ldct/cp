/*
PROG: paren
LANG: C++
ID: xuanji2
*/

#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <math.h>

#define MAGIC 12345678910

FILE *fin;
FILE *fout;

long long N;
long long n;

long long score() {

    long long s = 0;

    int p;
    fscanf(fin, "%d", &p);
    n++;
    if (p == 0) {
        s = (s + (2 * score())) % MAGIC;
    }
    if (p == 1)
        return 1;

    while (n < N) {
        int p;
        fscanf(fin, "%d", &p);
        n++;
        if (p == 0) {
            s = (s + (2 * score())); //DON'T put MAGIC HERE
        }
        if (p == 1)
            return s;
    }
    return s;
}

int main() {

    fin  = fopen("paren.in", "r");
    fout = fopen("paren.out", "w");

    fscanf(fin, "%lld\n", &N);
    n = 0;
    fprintf(fout, "%lld\n", (score() / 2) % MAGIC);
    return 0;
}
