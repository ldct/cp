class MillerRabin:
    def __init__(self):
        self._known_primes = [2, 3]
        self._known_primes += [x for x in range(5, 1000, 2) if self.is_prime(x)]

    def is_prime(self, n, _precision_for_huge_n=16):
        def _try_composite(a, d, n, s):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2**i * d, n) == n-1:
                    return False
            return True # n  is definitely composite

        if n in self._known_primes:
            return True
        if any((n % p) == 0 for p in self._known_primes) or n in (0, 1):
            return False
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1
        if n < 1373653:
            return not any(_try_composite(a, d, n, s) for a in (2, 3))
        if n < 25326001:
            return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
        if n < 2**64:
            return not any(_try_composite(a, d, n, s) for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022))

        # otherwise
        return not any(_try_composite(a, d, n, s)
                    for a in _known_primes[:_precision_for_huge_n])

mr = MillerRabin()
print([i for i in range(1,100) if mr.is_prime(i)])