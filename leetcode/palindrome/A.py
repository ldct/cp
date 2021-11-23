#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

def makePalindrome(n, odd):

    res = n
    if (odd):
        n = int(n / 10)
    while (n > 0):
        res = 10 * res + n % 10
        n = int(n / 10)
    return res

# Check if a number is palindrome
# in base k
def isPalindrome(n, base):
    reversed = 0
    temp = n
    while (temp > 0):
        reversed = reversed * base + temp % base
        temp = int(temp / base)

    return reversed == n

def sumPalindrome(num_first, k):

    i = 1
    n = 10
    palindromes = set()

    p = makePalindrome(i, True)

    for e in range(2, 100):
        n = 2**e
        if len(palindromes) >= num_first: break
        # print("e=", e)
        while (p < n):
            if (isPalindrome(p, k)):
                palindromes.add(p)
            i += 1

            p = makePalindrome(i, True)

        i = 1

        # loop for generation of
        # even palindromes
        p = makePalindrome(i, False)
        while (p < n):
            if (isPalindrome(p, k)):
                palindromes.add(p)
            i += 1
            p = makePalindrome(i, False)

    palindromes = sorted(list(palindromes))
    return palindromes

arr = []
for k in range(2, 10):
    arr += [sumPalindrome(30, k)]

print(arr)