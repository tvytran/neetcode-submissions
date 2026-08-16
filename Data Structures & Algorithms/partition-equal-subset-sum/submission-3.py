class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        

        target = sum(nums)//2
        dp = [False] * (target+1)
        dp[0] = True

        possible= [0]

        for n in nums:
            index = target-n
            while index > -1:
                if dp[index] == True:
                    dp[index +n] = True
                    if index +n== target:
                        return True
                index -=1
        return dp[target]  

            