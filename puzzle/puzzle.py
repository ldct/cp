#!/usr/bin/env python3

COMBINED = """jogger
hurdle
beside""".lower().split('\n')

WORDS1 = """ape
rat
sid
war""".lower().split('\n')

WORDS2 ="""cod
eon
era
led
one""".lower().split("\n")

for c in COMBINED:
    for w in WORDS1 + WORDS2:
        if w in c:
            print(c, w)
        if set(w).issubset(set(c)):
            print("match", c, w)
