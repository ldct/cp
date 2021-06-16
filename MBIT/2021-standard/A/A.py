input()
A = list(map(int,input().split()))
print(1+A[0]+A[-1]+sum(1+abs(A[i]-A[i+1]) for i in range(len(A))))