#!/usr/bin/env python3

N, M = input().split(' ')
N = int(N)
M = int(M)

winners = [] # winners[i] is the index of the candidate who won city i

def winning_index(arr):
    # returns index with largest entry, break ties by smallest index
    sort_by = [(-votes, candidate) for candidate, votes in enumerate(arr)]
    return sorted(sort_by)[0][1]

for i in range(M):
    votes_for_candidate = list(map(int, input().split(' ')))
    winners += [winning_index(votes_for_candidate)]

cvotes_for = [0]*N # cvf[i]: number of cities which voted for candidate i

for winner in winners:
    cvotes_for[winner] += 1

print(winning_index(cvotes_for) + 1)