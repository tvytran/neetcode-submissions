class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIST = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums), 1):
                if nums[i] < nums[j]:
                    LIST[i] = max(LIST[i], LIST[j]+1)
        return max(LIST)        

        
        