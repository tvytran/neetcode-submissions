class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        count = 0
        curr = intervals[0]
        print(intervals)

        for i in range(1,len(intervals)):
            other = intervals[i]
            
            if curr[1] > other[0] and curr[1] <= other[1] or other[1] > curr[0] and other[1] <= curr[1] or curr[0] == other[0] and curr[1] == other[1]:
                count +=1
                if other[1] < curr[1]:
                    curr = other
            else:
                curr=other


        return count
        