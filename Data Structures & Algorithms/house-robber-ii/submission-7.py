class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        def helper(cut):
            prev2 = 0
            prev = 0
            for i in range(len(cut)):
                curr = max(cut[i] +prev2, prev)
                prev2 = prev
                prev = curr
            return max(prev2, prev)

        return max(helper(nums[0:len(nums)-1]), helper(nums[1:]))


        