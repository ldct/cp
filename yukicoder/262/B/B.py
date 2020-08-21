#!/usr/bin/env pypy3

def y_given_x(x, A):
	ret = 0
	while x**ret < A:
		ret += 1
	return ret

def ans1(A):
	s1 = 2*y_given_x(2, A)
	s2 = 3*y_given_x(3, A)
	s3 = 5*y_given_x(5, A)
	s4 = 7*y_given_x(7, A)

	return min(s1, s2, s3, s4)

def ans2(A):
	s1 = 2*y_given_x(2, A)
	s2 = 3*y_given_x(3, A)

	return min(s1, s2)

A = int(input())
print(ans1(A))
