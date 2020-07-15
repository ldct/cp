#!/usr/bin/env python3

def cost(left, arr, right):
	i = 0
	j = len(arr)-1

	while i <= j:
		if arr[i] < left:
			i += 1
		elif arr[j] < right:
			j -= 1
		else:
			break

	if i > j:
		if Y*K <= X:
			return len(arr)*Y
		else:
			to_kill = len(arr)
			num_beserks = to_kill // K
			to_kill -= num_beserks*K

			return num_beserks*Y + to_kill*X

	assert(False)

	print(left, arr, right, i, j)
	return 0
	
def ans(A, B, K, X, Y):
	i = 0
	j = 0
	i_matches = []
	while i < len(A) and j < len(B):
		while i < len(A) and j < len(B) and A[i] != B[j]:
			i += 1
		i_matches += [i]
		j += 1

	if j != len(B): return -1

	assert(len(i_matches) >= 1)

	ret = 0

	ret += cost(float("-inf"), A[0:i_matches[0]], A[i_matches[0]])

	for j in range(len(i_matches)-1):
		p, q = i_matches[j], i_matches[j+1]
		ret += cost(A[p], A[p+1:q], A[q])

	ret += cost(A[i_matches[-1]], A[i_matches[-1]+1:], float("-inf"))

	return ret

N, M = input().split(' ')
N = int(N)
M = int(M)
X, K, Y = input().split(' ')
X = int(X)
K = int(K)
Y = int(Y)
A = input().split(' ')
A = list(map(int, A))
B = input().split(' ')
B = list(map(int, B))
print(ans(A, B, K, X, Y))
