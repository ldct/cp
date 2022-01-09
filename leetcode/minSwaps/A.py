#!/usr/bin/env pypy3

def minSwaps(data):
    count_one = sum(data)
    if count_one == 0:
        return 0

    n = len(data)
    cur = sum(data[:count_one])
    ans = cur
    for i in range(count_one, n):
        cur += data[i] - data[i - count_one]
        ans = max(ans, cur)

    return count_one - ans

def ms2(arr) :
    numberOfOnes = sum(arr)
    n = len(arr)

    # length of subarray
    # to check for
    x = numberOfOnes

    count_ones = 0
    maxOnes = 0

    # Find 1's for first
    # subarray of length x
    for i in range(0, x) :

        if(arr[i] == 1) :
            count_ones = count_ones + 1

    maxOnes = count_ones

    # using sliding window
    # technique to find
    # max number of ones in
    # subarray of length x
    for i in range(1, (n - x + 1)) :

        # first remove leading
        # element and check
        # if it is equal to 1
        # then decrement the
        # value of count_ones by 1
        if (arr[i - 1] == 1) :
            count_ones = count_ones - 1

        # Now add trailing
        # element and check
        # if it is equal to 1
        # Then increment
        # the value of count_ones by 1
        if(arr[i + x - 1] == 1) :
            count_ones = count_ones + 1

        if (maxOnes < count_ones) :
                maxOnes = count_ones

    # calculate number of
    # zeros in subarray
    # of length x with
    # maximum number of 1's
    numberOfZeroes = x - maxOnes

    return numberOfZeroes

print(ms2([1,1,0,0,1,1,0,0,0,0,1,1]))