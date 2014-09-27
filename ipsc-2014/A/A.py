#!/usr/bin/env python3

T = int(input(''))

def edit(P, q):
  ret = ''
  while not (P.startswith(q)):
    q = q[:-1]
    ret += '<'
  ret += P[len(q):]
  ret += '*'
  return ret

def rewrite(P, q):
  return "*{0}*".format(P)

def keys(P, Q):
  if len(rewrite(P, Q)) < len(edit(P, Q)):
    return rewrite(P, Q)
  else:
    return edit(P, Q)

for t in range(T):
  R = input('')
  P = input('')
  Q = input('')
  print(keys(P, Q))