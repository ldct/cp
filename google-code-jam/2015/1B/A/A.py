#!/usr/bin/env python

def num_uniqs(l):
	return len(set(l))

def characters_in(s):
	def characters_in_ignore(s, ignore):
		if s == "":
			return ""
		if s[0] == ignore:
			return characters_in_ignore(s[1:], ignore)
		else:
			return s[0] + characters_in_ignore(s[1:], s[0])
	return characters_in_ignore(s, "\n")

def run_length(s):
	if s == "":
		return []
	else:
		head = s[0]
		t = 0
		while t < len(s) and head == s[t]:
			t += 1
		return [t] + run_length(s[t:])

def min_to_match(l):
	l = sorted(l)
	mid = l[len(l) / 2]
	diff = map(lambda x: abs(x - mid), l)
	return sum(diff)

for t in range(int(raw_input(''))):
	N = int(raw_input(''))
	words = []
	for n in range(N):
		words += [raw_input('')]
	if num_uniqs(map(characters_in, words)) > 1:
		print "Case #%i: Fegla Won" % (t + 1)
	else:
		print "Case #%i: %i" % (t+1, sum(map(min_to_match, zip(*map(run_length, words)))))