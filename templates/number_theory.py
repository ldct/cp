def cdiv(x, y):
    # ceil(x / y)
    return x // y if x % y == 0 else x // y + 1

def cmod(x, M):
    # starting from x, search for the smallest multiple of M
    return M*cdiv(x, M)

# extended euclid
def egcd(a, b):
    """
    returns
    gcd(a, b), s, r
    s.t.
    a * s + b * r == gcd(a, b)
    """
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0

def multiplicative_partitions(n):
    from more_itertools import set_partitions
    ret = []
    for p in set_partitions(factorize(n)):
        m = list(map(product, p))
        ret += [tuple(sorted(m))]
    ret = list(set(ret))
    ret.sort()
    return ret

def modinv(a, m):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = egcd(a % m, m)
    return x % m if g == 1 else None

def pow2(A, B, C, MODULUS):
    # A^(B^C), prime MODULUS
    A %= MODULUS
    if A == 0: return 0
    BC = pow(B, C, MODULUS-1)
    return pow(A, BC, MODULUS)

# integer square root
def isqrt(n):
    if n > 0:
        x = 1 << (n.bit_length() + 1 >> 1)
        while True:
            y = (x + n // x) >> 1
            if y >= x:
                return x
            x = y
    elif n == 0:
        return 0
    else:
        raise ValueError("square root not defined for negative numbers")

# O(sqrt n) factorization
def factorize(n):
    N = n
    ret = []
    i = 2
    while i<=n:
        if i * i > N:
            ret.append(n)
            break
        if n%i==0:
            ret.append(i)
            n//= i
        else:
            i+=1
    return ret

# untested

def count_multiples(A, B, c):
    # number of multiples of c in [A, B]
    return B//c - (A-1)//c

def divisors(n):
    ret = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            ret += [i]
            if i*i != n:
                divisors += [n / i]
    return ret

def s0(n):
    ret = 0
    for d in range(1,n+1):
        if n%d == 0:
            ret += 1
    return ret
