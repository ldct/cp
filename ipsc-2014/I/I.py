#!/usr/bin/env python3

import heapq

T = int(input(''))

def encoding(parent):
  return parent

def flatsum(arr):
  try:
    ret = 0
    for a in arr:
      if isinstance(a, int) or isinstance(a, float):
        ret += a
      else:
        ret += flatsum(a)
    return ret
  except Exception as e:
    return arr

def indices_of_smallest_two(arr):
  arr = [(a, i) for (i, a) in enumerate(arr)]
  arr = sorted(arr)
  return (arr[0][1], arr[1][1])

def huffman(weights):
  while len(weights) > 1:
    print(weights)
    sum_of_weights = list(map(flatsum, weights))
    (a, b) = sorted(indices_of_smallest_two(sum_of_weights))
    weights += [(weights[a], weights[b])]
    del weights[b]
    del weights[a]
  return weights

for t in range(T):
  R = input('')
  N = input('')
  parent = ['0', '0'] + input('').split(' ')
  parent = list(map(int, parent))
  #print(encoding(parent))
  print(huffman([0.4, 0.35, 0.2, 0.05]))