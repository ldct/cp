#!/usr/bin/env python3

def get_ints():
    return map(int, input('').split(' '))

def smallest(N):
    n_str = list(str(N))

    smallest_digit = n_str[0]
    smallest_pos = 0
    for i in range(len(n_str))[::-1]:
        if n_str[i] != '0' and int(n_str[i]) < int(smallest_digit):
            smallest_digit = n_str[i]
            smallest_pos = i
    # print(smallest_digit, smallest_pos)
    n_str[0], n_str[smallest_pos] = n_str[smallest_pos], n_str[0]
    return ''.join(n_str)

def largest(N):
    n_str = list(str(N))

    largest_digit = n_str[0]
    largest_pos = 0
    for i in range(len(n_str))[::-1]:
        if n_str[i] != '0' and int(n_str[i]) > int(largest_digit):
            largest_digit = n_str[i]
            largest_pos = i
    # print(largest_digit, largest_pos)
    n_str[0], n_str[largest_pos] = n_str[largest_pos], n_str[0]
    return ''.join(n_str)

for t in range(int(input(''))):
    (N, ) = get_ints()
    print("Case #%d: %s %s" % (t + 1, smallest(N), largest(N)))