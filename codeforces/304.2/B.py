from collections import defaultdict

N = input()
a = input().split(' ')
a = map(int, a)

counts = defaultdict(int)
for e in a:
    counts[e] += 1

cost = 0
cont = True

while cont:
    cont = False
    for e in counts:
        if counts[e] > 1:
            counts[e + 1] += counts[e] - 1
            cost += counts[e] - 1
            counts[e] = 1
            cont = True
            break

print(cost)