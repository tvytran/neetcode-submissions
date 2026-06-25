class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = nums[0]
        currmin = nums[0]
        gmax = currmax
        for i in range(1,len(nums)):
            amin = currmin * nums[i]
            amax = currmax * nums[i]

            currmin = min(amin, amax, nums[i])
            currmax = max(amin, amax, nums[i])

            if currmax > gmax:
                gmax = currmax

        return gmax
            