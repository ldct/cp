#!/usr/bin/env pypy3

def inty(s):
    try:
        return int(s)
    except ValueError:
        return None

from functools import reduce

def split(iterable, where):
    def splitter(acc, item, where=where):
        if item == where:
            acc.append([])
        else:
            acc[-1].append(item)
        return acc
    return reduce(splitter, iterable, [[]])

import sys

lst = []
for line in sys.stdin:
    lst += [line[:-1]]

def is_valid(passport):

    byr = list(field for field in passport if field.startswith("byr"))
    if len(byr) == 0: return False
    [byr] = byr
    byr = byr.split(":")[1]
    byr = int(byr)
    if not (1920 <= byr <= 2002): return False

    iyr = list(field for field in passport if field.startswith("iyr"))
    if len(iyr) == 0: return False
    [iyr] = iyr
    iyr = iyr.split(":")[1]
    iyr = int(iyr)
    if not (2010 <= iyr <= 2020): return False

    eyr = list(field for field in passport if field.startswith("eyr"))
    if len(eyr) == 0: return False
    [eyr] = eyr
    eyr = eyr.split(":")[1]
    eyr = int(eyr)
    if not (2020 <= eyr <= 2030): return False

    hgt = list(field for field in passport if field.startswith("hgt"))
    if len(hgt) == 0: return False
    [hgt] = hgt
    hgt = hgt.split(":")[1]
    if not (hgt[-2:] in ["cm", "in"]): return False
    if hgt[-2:] == "cm":
        if not (150 <= int(hgt[:-2]) <= 193): return False
    if hgt[-2:] == "in":
        if not (59 <= int(hgt[:-2]) <= 76): return False

    hcl = list(field for field in passport if field.startswith("hcl"))
    if len(hcl) == 0: return False
    [hcl] = hcl
    hcl = hcl.split(":")[1]
    if not hcl.startswith("#"): return False
    hcl = hcl[1:]
    if not len(hcl) == 6: return False
    for c in hcl:
        if c not in "0123456789abcdef": return False

    ecl = list(field for field in passport if field.startswith("ecl"))
    if len(ecl) == 0: return False
    [ecl] = ecl
    ecl = ecl.split(":")[1]
    if not ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False

    pid = list(field for field in passport if field.startswith("pid"))
    if len(pid) == 0: return False
    [pid] = pid
    pid = pid.split(":")[1]
    if len(pid) != 9: return False
    for c in pid:
        if c not in "0123456789": return False

    return True

ret = 0

for passport in split(lst, ''):
    passport = [s.split(' ') for s in passport]
    joined = []
    for fields in passport:
        joined += fields
    passport = joined
    if is_valid(passport):
        ret += 1

print(ret)