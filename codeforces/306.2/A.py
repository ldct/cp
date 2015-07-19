#!/usr/bin/env python3
import re
S = input()

if S.find("AB") >= 0 and "BA" in S[S.find("AB") + 2:]:
    print("YES")
elif S.find("BA") >= 0 and "AB" in S[S.find("BA") + 2:]:
    print("YES")
else:
    print("NO")