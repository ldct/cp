import math
 
A, B = input().split(' ')
A = int(A)
B = int(B)
 
A -= 1
B -= 1
 
print(math.ceil(B / A))
