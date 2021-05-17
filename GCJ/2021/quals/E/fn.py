#!/usr/bin/env python3

t = int(input())
p = int(input())
for test in range(1, t + 1):
    mat = []
    for _ in range(100):
        mat.append(list(input()))

    col_sum = []
    for j in range(10000):
        curr_sum = 0
        for i in range(100):
            if mat[i][j] == 1:
                curr_sum += 1
        col_sum.append([curr_sum/100, j])


    col_sum = sorted(col_sum)[::-1]

    horz_ls = []
    for i in range(100):
        curr_sum = 0
        for j in range(100):
            if mat[i][col_sum[j][1]] == 1:
                curr_sum += 1
        horz_ls.append([curr_sum,i])

    horz_ls = sorted(horz_ls)
    print(horz_ls)
    res = sorted(horz_ls)[::-1][0][1] + 1

    print(f"Case #{test}: {res}")