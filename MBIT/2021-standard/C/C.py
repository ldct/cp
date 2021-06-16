def f(a):
    t = a[0].isupper()
    a = list(a.lower())[::-1]
    if t: a[0]=a[0].upper()
    return ''.join(a)
print(' '.join(list(map(f, input().split()))[::-1]))