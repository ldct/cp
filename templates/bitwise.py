def perm(mask):
    subset = []

    for i in range(N):
        if mask & (1 << i):
            subset += [i+1]

    return subset

def subsets(mask):
    ret = []
    for i in range(N):
        if 0 == mask & (1 << i): continue
        ns = mask & ~(1 << i)
        ret += [ns]

    return ret
