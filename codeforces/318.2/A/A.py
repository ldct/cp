#!/usr/bin/env python3
import sys

N = input()
votes = list(map(int, input().split()))

def num_bribes():
    bribes = 0


    while True:

        most_votes, winner = sorted((votes, idx) for idx, votes in enumerate(votes))[-1]
        my_votes = votes[0]
        num_most_voted = sum(1 for vote in votes if vote == most_votes)

        if my_votes == most_votes and num_most_voted == 1:
            return bribes

        else:
            diff = 1
            bribes += diff
            votes[0] += diff
            votes[winner] -= diff

print(num_bribes())