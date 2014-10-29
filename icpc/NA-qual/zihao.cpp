#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <bitset>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

int N;

struct C { string u1,u2; int c; };

bool cmp(C a, C b) { return a.c > b.c; }

int main() {
	while(cin >> N && N) {
		vector<C> vc;
		for(int i=0;i!=N;i++) {
			string s; cin >> s;
		}
		for(int i=0;i!=N-1;i++) {
			char u1[10]={0};
			char u2[10]={0};
			C c;
			scanf("%s = %d %s",u1,&c.c,u2);
			c.u1 = u1;
			c.u2 = u2;
			vc.push_back(c);
		}

		int cg = 1;
		while(cg) {
			cg= 0;
			for(int i=0;i!=vc.size();i++) {
				for(int j=0;j!=vc.size();j++)
					if(i!=j) {
						if(vc[i].u1 == vc[j].u2) {
							vc[j].u2 = vc[i].u2;
							vc[j].c *= vc[i].c;
							cg = true;
						}
					}
				}
				for(int i=0;i!=vc.size();i++) {
					for(int j=0;j!=vc.size();j++)if(i!=j) {
						if(vc[i].u1 == vc[j].u1) {
							int a=i,b=j;
							if(vc[i].c > vc[j].c)
								swap(a,b);
								vc[a].u1 = vc[a].u2;
								vc[a].u2 = vc[b].u2;
								vc[a].c = vc[b].c/vc[a].c;
								cg = true;
							}
						}
					}
				}
				sort(vc.begin(),vc.end(),cmp);
				cout << 1 << vc[0].u1;
				for(int i=1;i!=vc.size();i++) {
					cout << " = ";
					cout << vc[0].c / vc[i].c;
					cout << vc[i].u1;
				}
				cout << " = ";
				cout << vc[0].c << vc[0].u2 << endl;
			} return 0;
		}