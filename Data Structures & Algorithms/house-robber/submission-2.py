class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev = 0

        for num in nums:
            curr = 0
            if num + prev2 > prev:
                curr = num+prev2
            else:
                curr = prev
            prev2 = prev
            prev = curr
        
        return max(prev2, prev)



        