# minimum e>=0 such that e is not contained in A
def mex(A):
    if len(A) == 0:
        return 0
    sA = set(A)
    for i in range(0, max(A+[0])+1):
        if i not in sA:
            return i
    assert(False)