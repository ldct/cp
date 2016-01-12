# Deriving Fenwick Trees

Given an array A, we want to create a data structure that supports the following operations:

1. Update: for some (i, v), set A[i] += v
2. Prefix sum: for some i, return sum(A[0:i])

If we simply use the original array A, (1) takes O(1) time and (2) takes O(N) time, where N is the length of the array. With Fenwick tree, both operations take O(log N) time.

If we instead precompute the prefix sum array P which satisfies P[i] = sum(A[0:i]), which takes time O(N), then (2) takes O(1) time, but (1) takes O(N) time.

So to get both operations to O(log N), we take the second idea and deliberately try to make (2) a bit more inefficient. Instead of storing sum(A[0:i]) for all values of i, maybe we should store sum(A[a:b]) for some subset of pairs of (a, b). Then if we choose our subset carefully, we can use our stored values to recover sum(A[0:i]) in O(log N) time. (Interesting fact: if we choose a, b to be consecutive multiples of sqrt(N), then both operations take O(sqrt N))

If we are to be able to recover sum(A[0:i]) for all i, then in our subset of pairs there must be a sequence (0, a_1), (a_1, a_2) ... (a_k, i).

One way to enforce this constraint is to form a min-heap of the endpoint indices {O...N}, where if there is an edge from x -> y, then we store sum(A[x:y]). Then the cost of (2) is O(depth of min-heap), so to get O(log N) the heap should be balanced.

At this point we could continue trying to derive what heap to use, but it's simpler to think about why the Fenwick heap works:

http://codeforces.com/predownloaded/db/c7/dbc733901aa8c6b312d5677686422d35daaae8a0.png

Construction: a node x has children x+1, x+2, x+4, x+8...

First, note that it has the nice (but not strictly necessary property) that if we add more elements to the heap, we don't need to destroy any existing edges.

Second, it is actually a search tree as well: for two siblings a and b, if a is to the left of b, then all subchildren of a are less than all subchildren of b. This makes update efficient. When we perform A[i] += v, if we ever need to update the interval a -> b then we never need to update any edge in the subtree of a sibling of a, because if the sibling is on a's left, then every edge in that subtree has endpoints less than a, and similarly for if the sibling is on b's right.

http://petr-mitrichev.blogspot.com/2013/05/fenwick-tree-range-updates.html