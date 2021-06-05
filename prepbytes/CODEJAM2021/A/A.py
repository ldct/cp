#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def ans(H, M):
    H %= 12

    h_angle = (H * 60 + M) // 2
    m_angle = 6 * M

    h_angle = int(h_angle) % 360
    m_angle = int(m_angle) % 360

    angle = abs(h_angle - m_angle)
    return int(min(angle, 360-angle))

for _ in range(read_int()):
    H, M = read_int_tuple()
    print(ans(H, M))