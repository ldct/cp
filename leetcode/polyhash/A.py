#!/usr/bin/env pypy3

S = "dlojuxgftvpqpsknfgkejydsxgcgyroavsefjrejytcgflrnnxxsxowqbteycujnrbaokjibq"
P = 8
MODULUS = 54
K = 30
TARGET = 16

def val(c):
    return ord(c) - ord('a') + 1

def hv(s):
    return sum([val(c)*pow(P, i, MODULUS) for (i, c) in enumerate(s)]) % MODULUS

# print(hv("kejydsxgcgyroavsefjrejytcgflrn"))
# print(hv("kejydsxgcgyroavsefjrejytcgflrn") * pow(P, S.index("kejydsxgcgyroavsefjrejytcgflrn"), MODULUS) % MODULUS)

class Solution:
    def subStrHash(self, s, power, MODULUS, k, target) -> str:

        def hv(s):
            return sum([val(c)*pow(power, i, MODULUS) for (i, c) in enumerate(s)]) % MODULUS

        ch = [val(c)*pow(power, i, MODULUS) for (i, c) in enumerate(s)]
        prefixes = [0]
        for n in ch:
            prefixes += [prefixes[-1] + n]

        for i in range(len(prefixes) - k):
            if (prefixes[i+k] - prefixes[i]) % MODULUS == (target * pow(power, i, MODULUS)) % MODULUS:
                if hv(s[i:i+k]) == target:
                    return s[i:i+k]

s = Solution()
print(s.subStrHash(S, P, MODULUS, K, TARGET))