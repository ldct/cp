N = input()
s1 = input().split(' ')[1:]
s2 = input().split(' ')[1:]

s1 = tuple(map(int, s1))
s2 = tuple(map(int, s2))

already_seen = set()
num_fights = 0

while len(s1) > 0 and len(s2) > 0:

    num_fights += 1

    if (s1, s2) in already_seen:
        break
    else:
        already_seen.add((s1, s2))

    if s1[0] < s2[0]:
        s2 = s2[1:] + (s1[0], s2[0])
        s1 = s1[1:]
    else:
        s1 = s1[1:] + (s2[0], s1[0])
        s2 = s2[1:]

if len(s1) == 0:
    print(str(num_fights) + ' 2')
elif len(s2) == 0:
    print(str(num_fights) + ' 1')
else:
    print(-1)