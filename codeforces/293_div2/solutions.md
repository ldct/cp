## Ilya and Escalator

Z(t, n) = Probability that at time t, there are n people on the escalator

Z(0, 0) = 1
Z(0, n) = 0 for n > 0

Z(t, N) = Z(t - 1, N) + p Z (t - 1, N - 1)
Z(t, n) = (1 - p) Z(t - 1, n) + p Z(t - 1, n - 1)