N = 100000
print(N)
print(' '.join(str(i) for i in range(N)))
print(' '.join(str(i % 199 + 1) for i in range(N)))