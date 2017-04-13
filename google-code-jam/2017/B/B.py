#!/usr/bin/env python3

T = int(input())

def last_tidy(S):
	blocks = []

	last_char = S[0]

	last_char_cnt = 0

	for c in S:
		if c == last_char:
			last_char_cnt += 1
		else:
			blocks += ((int(last_char), last_char_cnt), )
			last_char = c
			last_char_cnt = 1

	blocks += ((int(last_char), last_char_cnt), )

	i = 1

	while True:
		if i == len(blocks):
			return S
		if blocks[i][0] < blocks[i-1][0]:
			break
		assert(blocks[i][0] > blocks[i-1][0])
		i += 1


	assert(blocks[i-1][0] > 0)

	blocks = blocks[0:i-1] + [(blocks[i-1][0] - 1, 1), (9, blocks[i-1][1] - 1)] + blocks[i:]

	for j in range(i, len(blocks)):
		blocks[j] = (9, blocks[j][1])

	for i in range(len(blocks)):
		c, c_cnt = blocks[i]
		blocks[i] = str(c) * c_cnt

	return ''.join(blocks).lstrip('0')

for i in range(T):
	S = input()
	print("Case #" + str(i+1) + ": " + str(last_tidy(S)))
