class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        length = float('inf')
        total = 0
        while r < len(nums):
            total += nums[r]
            #print("total", total)
            if total < target:
                r +=1

            if total >= target and l <= r:
                while total >= target and l <= r:
                    length = min(length, r-l+1)
                    total -= nums[l]
                    l +=1

                if total > 0:
                    total -= nums[r]
                if r < l:
                    r = l
        
        if length == float('inf'):
            return 0
        return length
        