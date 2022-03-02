
def comb(n, r):
    return factorial(n) / factorial(r) / factorial(n-r)

def ans(T, K):

    T -= 1
    weight = dict()

    for score in range(T+1):
        weight[score] = comb(T, score)

    @lru_cache(None)
    def dp(K, curr):
        if curr == T: return curr
        if K == 0: return curr

        expected_next = 0
        for score in weight:
            expected_next += weight[score] * dp(K-1, score)
        expected_next /= (2**T)

        return max(curr, expected_next)

    # for k in range(K+1):
    #     print([dp(k, curr) for curr in range(K)])


    return 1 + dp(K, 0)