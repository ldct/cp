num_factors_memo = {}

def num_factors(n):
    if n <= 3:
        return 1

    if n in num_factors_memo:
        return num_factors_memo[n]

    for i in range(2, n):
        if i*i > n: return 1
        if n % i == 0:
            num_factors_memo[n] = 1 + num_factors(n // i)
            return num_factors_memo[n]



for i in range(5000000):
    if num_factors(i) == 1:
        print(i)

def solve(a, b):
    return 0

t = int(input())
for i in range(t):
    (a, b) = input().split(' ')
    a = int(a)
    b = int(b)
    # print(solve(a, b))
    # print(a, b)