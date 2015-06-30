#!/usr/bin/env python3

N = int(input())
min1, max1 = tuple(map(int, input().split(' ')))
min2, max2 = tuple(map(int, input().split(' ')))
min3, max3 = tuple(map(int, input().split(' ')))

ans1, ans2, ans3 = min1, min2, min3

def left():
	return N - (ans1 + ans2 + ans3)

ans1 += min(left(), max1 - ans1)
ans2 += min(left(), max2 - ans2)
ans3 += min(left(), max3 - ans3)

print(ans1, ans2, ans3)