# merge a list of overlapping intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for [a,b] in intervals:
            events += [(a, -1)]
            events += [(b, +1)]

        events = sorted(events)

        (start, count) = events[0]
        count = -count

        ret = []

        for (x, d) in events[1:]:
            print(f"{x} {count}")
            count -= d
            if count == 0:
                ret += [(start, x)]
            elif d == -1 and count == 1:
                start = x

        return ret