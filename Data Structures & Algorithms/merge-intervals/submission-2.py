class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        inter = deque(intervals)
        
        result = []

        compare = inter.popleft()
        while inter:
            other = inter.popleft()
            print(other)
            if compare[1] >= other[0] and compare[1] <= other[1] or other[1] >= compare[0] and other[1] <= compare[1]:
                compare = [min(other[0],compare[0]), max(other[1],compare[1])]
            else:
                result.append(compare)
                compare = other
        result.append(compare)
        return result
