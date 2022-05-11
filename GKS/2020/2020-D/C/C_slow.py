#!/usr/bin/env python2

from __future__ import division, print_function

import itertools
import sys

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

class Tree:
	def __init__(self, id):
		self.id = id
		self.parent = None
		self.children = set()

	def set_parent(self, parent):
		self.parent = parent
		parent.children.add(self)

	def path_to_root(self):
		ret = []
		node = self

		while node.parent:
			ret += [node.id]
			node = node.parent

		ret += [node.id]

		return ret

def ans(parents, N, A, B):
	trees = []
	for i in range(N):
		trees += [Tree(i)]

	for i, p in enumerate(parents):
		trees[i+1].set_parent(trees[p-1])

	num_painted = 0

	for i in range(N):
		for j in range(N):
			A_painted = trees[i].path_to_root()[::A]
			B_painted = trees[j].path_to_root()[::B]

			num_painted += len(set(A_painted + B_painted))

	return num_painted / (N*N)

	return parents

T = int(input())
for t in range(T):
	N, A, B = input().split(' ')
	N = int(N)
	A = int(A)
	B = int(B)

	parents = input().split(' ')
	parents = list(map(int, parents))

	print("Case #" + str(t+1) + ": " + str(ans(parents, N, A, B)))
