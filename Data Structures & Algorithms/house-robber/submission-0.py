class Solution:
    def rob(self, nums: List[int]) -> int:
        total = 0
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        return max(nums[len(nums)-1],nums[len(nums)-2])


        