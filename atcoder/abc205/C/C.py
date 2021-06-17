A,B,C = map(int,input().split())
C=C%2+2
n=pow(A,C)-pow(B, C)
print("<"if n<0 else "="if n==0 else ">")