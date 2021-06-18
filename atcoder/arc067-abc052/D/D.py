N,A,B,*X=map(int,open(0).read().split())
print(sum(min(A*(X[i+1]-X[i]), B) for i in range(N-1)))