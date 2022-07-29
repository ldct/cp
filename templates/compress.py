# coordinate compress a list with no repeated elements
def compress(arr):
    d = dict()
    for i, e in enumerate(sorted(arr)):
        d[e] = i
    return [d[e] for e in arr]