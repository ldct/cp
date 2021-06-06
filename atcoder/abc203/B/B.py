N,K=input().split()
print(sum(int(f"{i}0{j}") for i in range(1,int(N)+1) for j in range(1,int(K)+1)))