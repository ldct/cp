#!/usr/bin/env pypy3
n=10**7
l=[0]+[1]*n
for i in range(2,n+1):
    j=i
    while(j<=n):
        l[j]+=i
        j+=i
l1=[-1]*(n+1)
for i in range(n,0,-1):
    if(l[i]<=n):
        l1[l[i]]=i
