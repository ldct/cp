#!/usr/bin/env python3

from fractions import gcd

for t in range(int(input(''))):
    line = input('').split('/')
    P = int(line[0])
    Q = int(line[1])
    g = gcd(P, Q)
    P = int(P / g)
    Q = int(Q / g)

    P_bin = "{0:b}".format(P)
    Q_bin = "{0:b}".format(Q)

    if len(Q_bin.split("1")) > 2:
        print("Case #%i: impossible" % (t + 1))
    else:
        print("Case #%i: %i" % (t + 1, len(Q_bin) - len(P_bin)))