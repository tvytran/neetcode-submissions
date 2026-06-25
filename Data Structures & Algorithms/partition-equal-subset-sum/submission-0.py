class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = int(sum(nums))
        if total %2 == 1:
            return False
        target = total//2
        print("target = ", target)

        dp = [False] * (target+1)
        dp[0] = True

        for n in nums:
            index = target - n
            while index > -1:
                if dp[index] == True:
                    dp[index+n] = True
                    if index+n == target:
                        return True
            
                index -=1
        return False