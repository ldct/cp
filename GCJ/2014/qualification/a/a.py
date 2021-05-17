#!/usr/bin/env python3

T = int(input(''))

for i in range(T):
    first_answer = int(input(''))
    lines = {}
    for j in range(4):
        lines[j + 1] = input('')
    first_lines = lines[first_answer].split(' ')
    first_lines = set([int(k) for k in first_lines])

    second_answer = int(input(''))
    lines = {}
    for j in range(4):
        lines[j + 1] = input('')
    second_lines = lines[second_answer].split(' ')
    second_lines = set([int(k) for k in second_lines])

    candidates = first_lines & second_lines

    if len(candidates) == 0:
        print("Case #%d: Volunteer cheated!" % (i + 1))
    elif len(candidates) == 1:
        print("Case #%d: %d" % (i + 1, list(candidates)[0]))
    else:
        print("Case #%d: Bad magician!" % (i + 1))