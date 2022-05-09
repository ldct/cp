def ss(target, B):
    import array
    possible = array.array('b', [1] + [0]*target)

    for b in B:
        next_possible = array.array('b', possible)
        for i in range(target):
            if possible[i] == 1 and i + b <= target:
                next_possible[i+b] = 1
        possible = next_possible

    return possible

def ss_ncp(target, B):
    import array
    possible = array.array('b', [1] + [0]*target)

    for b in B:
        for mass in range(target, -1, -1):
            if possible[mass] == 1 and mass + b <= target:
                possible[mass+b] = 1
    return possible