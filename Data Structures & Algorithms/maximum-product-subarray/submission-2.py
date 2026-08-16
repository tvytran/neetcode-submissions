class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin = 1
        currMax = 1

        for n in nums:
            
            tmp = currMax * n
            currMax = max(currMax *n, currMin * n, n)
            currMin = min(tmp, currMin *n, n)

            res = max(currMax, res)
        
        return res