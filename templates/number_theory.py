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


def modinv(a, m):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = egcd(a % m, m)
    return x % m if g == 1 else None

# untested

def count_multiples(A, B, c):
    # number of multiples of c in [A, B]
    return B//c - (A-1)//c

def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def s0(n):
    ret = 0
    for d in range(1,n+1):
        if n%d == 0:
            ret += 1
    return ret