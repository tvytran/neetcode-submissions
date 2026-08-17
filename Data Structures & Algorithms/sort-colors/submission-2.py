class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums)-1
        mid = 0 
        while mid < len(nums):
            if nums[mid] == 0:
                tmp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = tmp
                low += 1
                mid += 1
            elif mid < high and nums[mid] == 2:
                print(nums)
                tmp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = tmp
                high-=1
                print(nums)
            else:
                mid +=1
        
                