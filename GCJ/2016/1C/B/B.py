#!/usr/bin/env python

T = int(raw_input())

def ans(B, M):
	if M > 2**(B-2):
		return None
	ret = []
	for _  in range(B):
		ret += [[0] * B]

	for i in range(B-1):
		for j in range(i+1, B-1):
			ret[i][j] = 1

	# fully connected

	for i in range(B-1):
		ret[i][B-1] = 1

	deletes = 2**(B-2) - M
	binary = format(deletes, '#0' + str(B) + 'b')[2::]

	# print('removing', binary)

	for i, d in enumerate(binary[::-1]):
		if d == '1':
			ret[i+1][B-1] = 0

	return ret

for t in range(T):
	B, M = [int(i) for i in raw_input().split(' ')]
	the_ans = ans(B, M)
	if the_ans is None:
		print("Case #{0}: {1}".format(t+1, 'IMPOSSIBLE'))
	else:
		print("Case #{0}: {1}".format(t+1, 'POSSIBLE'))
		for row in the_ans:
			print(''.join(str(i) for i in row))
