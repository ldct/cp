S = int(input())
while S>0 and (S%10==0): S//=10
S=str(S)
print("Yes" if S == S[::-1] else "No")
