def wp(ret, k):
    ret = list(ret)

    i = 0
    while ret[i] != -1 and i < len(ret): i += 1
    if i == len(ret): return False

    if k > 1:
        ret[i] = k
        if i+k >= len(ret) or ret[i+k] != -1: return False
        ret[i+k] = k
    else:
        ret[i] = k

    return ret

def ans2(start, remains):
    if len(remains) == 0: return start

    for k in sorted(remains)[::-1]:
        partial = wp(start, k)
        if partial:
            c = ans2(partial, [r for r in remains if r != k])
            if c:
                return c

def ans(n):
    return ans2(
        [-1]*(2*n-1),
        list(range(1, n+1))
    )

for i in range(1,50):
    print(ans(i))
