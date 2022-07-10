from itertools import chain, combinations

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

print(list(subsets([1,2,3], 2, 2)))

def subsequences(S):
    ret = []
    for indices in subsets(range(len(S))):
        ret += [[S[i] for i in indices]]
    return ret

def is_subsequence(needle, haystack):
    current_pos = 0
    for c in needle:
        current_pos = find(haystack, c, current_pos) + 1
        if current_pos == 0:
            return False
    return True

## shim for math.comb
def comb(n, r):
    if r > n: return 0
    if r == 0: return 1
    if r == 1: return n
    if r == 2: return n*(n-1)//2
    return reduce(op.mul, range(n - r + 1, n + 1), 1) // math.factorial(r)


def count_partitions_interval(n, N, l=0, r=None):
    """
    Number of tuples x_1, x_2 ... x_n such that
    x_i \in [l, r]
    \sum x_i = N
    aka extended stars and bars
    https://math.stackexchange.com/questions/553960/extended-stars-and-bars-problemwhere-the-upper-limit-of-the-variable-is-bounded

    tag:combinatorics tag:generating-functions tag:number-theory
    """

    if r is None: r = N

    N -= n*l
    r -= l

    ret = 0
    UB = min(n, N // (r+1))
    for q in range(0, 1+UB):
        ret += (-1)**q * comb(n, q) * comb(N - q*(r+1) + n-1, n-1)
    return ret

def cost(word):
    """
    Smallest number of cyclic shifts to make the word equal to the starting value
    cost("abcd") == 4
    cost("abab") == 2
    """    
    word = ''.join(word)
    haystack = (word + word)[1:]
    return 1 + haystack.index(word)

def cycles(perm):
    remain = set(perm)
    result = []
    while len(remain) > 0:
        n = remain.pop()
        cycle = [n]
        while True:
            n = perm[n]
            if n not in remain:
                break
            remain.remove(n)
            cycle.append(n)
        result.append(cycle)
    return result
