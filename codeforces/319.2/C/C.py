#!/usr/bin/env python3

N = int(input())

is_prime = [True]*(N+1)

primes = set()

for i in range(2, N+1):
  if is_prime[i]:
    for j in range(i, N+1, i):
      is_prime[j] = False
    primes.add(i)

ans = set()

for p in primes:
  for k in range(1, N + 1):
    if p**k <= N:
      ans.add(p**k)
    else:
      break

print(len(ans))
print(' '.join(str(x) for x in ans))