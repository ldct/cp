import math

A = input()
B = input()

ret = 0

for i in range(3):
    if A[i] == B[i]:
        ret += 1

print(ret)