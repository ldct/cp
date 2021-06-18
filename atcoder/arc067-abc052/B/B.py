input()
S=[{'I':1,'D':-1}[i] for i in input()]
print(max(sum(S[:i]) for i in range(1+len(S))))