#!/usr/bin/env python3

T = int(input(''))

def original(end):
  seen_so_far = set()
  ret = []
  for i in end:
    if i not in seen_so_far:
      ret += [i]
      seen_so_far |= {i}
  return ' '.join(map(str, ret))

for t in range(T):
  R = input('')
  N = int(input(''))
  end = map(int, input('').split(' '))
  print(original(end))