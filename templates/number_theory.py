def cdiv(x, y):
    # ceil(x / y)
    return x // y if x % y == 0 else x // y + 1

def cmod(x, M):
    # starting from x, search for the smallest multiple of M
    return M*cdiv(x, M)

# untested

def count_multiples(A, B, c):
    # number of multiples of c in [A, B]
    return B//c - (A-1)//c