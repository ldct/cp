#TAG:histogram

def prevSmall(arr):
    """
    ret[i] is the index of the smallest j <= i such that arr[j] < arr[i], or -1 if no such j exists
    """
    S = [(-1,-1)]
    ret = []
    for i,a in enumerate(arr):
        # ensure S + [arr[i]] is strictly increasing
        while S[-1][0] >= a: S.pop()
        ret += [S[-1][1]]
        S += [(a, i)]

    return ret

def nextSmall(arr):
    return [len(arr) - 1 - i for i in prevSmall(arr[::-1])][::-1]

def largestRectangleArea(self, heights: List[int]) -> int:
    ps = prevSmall(heights)
    ns = nextSmall(heights)

    ret = 0

    for idx, (i, j) in enumerate(zip(ps, ns)):
        ret = max(ret, heights[idx]*(j-i-1))

    return ret