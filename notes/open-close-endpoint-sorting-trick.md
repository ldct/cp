# Open-Close Endpoint Sorting Trick

Consider this problem (which is a 1-D simplification of http://codeforces.com/problemset/problem/610/D)

Vika has an infinite roll of toilet paper, ie a list of squares, each of which has a square to the left and to the right. Initially all squares are white. She introduced a one-dimensional coordinate system on this sheet and drew n black horizontal. All segments have width equal to 1 square, that means every segment occupy some set of neighbouring squares situated in one row. Your task is to calculate the number of painted cells. If a cell was painted more than once, it should be calculated exactly once.

The number of segments is small, but the coordinates of each endpoint is unbounded.

Solution: imagine we want to know how many times each cell is painted. Consider the case

0 5
1 8
20 23

Then cells [1, 2, 3, 4, 5] are painted twice, cells [0, 6, 7, 8, 20, 21, 22, 23] are painted once, everything else is painted 0 times. This produces the same pattern as if the input were

0 8
1 5
20 23

In fact, the pairing doesn't matter, we can reconstruct the painting using this information

0 - start
1 - start
5 - stop
8 - stop
20 - start
23 - stop

which we constructed by putting "start" next to every segment LHS and "stop" next to every segment RHS and then sorting. Then Vika can start at 0, keep track of number of times current cell is to be painted = n = #(starts encounted so far) - #(stops encountered so far). Eg at position 2, n = 2, which means cell 2 was painted 2 times. Now each for each segment S in [0, 1), [1, 5), [5, 8) etc, all cells in S have the same n. Then we just add up the lengths of all segments for which n > 0.


https://github.com/lamphanviet/competitive-programming/blob/master/light-online-judge/accepted-solutions/1120%20-%20Rectangle%20Union.cpp
http://codeforces.com/blog/DanAlex
http://zobayer.blogspot.sg/2013/11/various-usage-of-bit.html
http://arxiv.org/pdf/1311.6093v4.pdf
