class Solution:
    def longestConsecutive(self, nums: List[int]):
        counts = {}
        for n in nums:
            if n not in counts:
                counts[n] = 0
            counts[n] +=1
        
        long = 0
        for n in nums:
            if n-1 not in counts:
                start = 0
                while n in counts and counts[n] > 0:
                    counts[n] -=1
                    start +=1
                    n+=1
                long = max(long, start)
        
        return long
                
        