#!/usr/bin/env python3

def numshovels(price, spare_coin_denom):
	for i in range(1, 11):
		spare_needed = i*price % 10
		if spare_needed in [0, spare_coin_denom]:
			return i

(a, b) = input().split(' ')
print(numshovels(int(a), int(b)))