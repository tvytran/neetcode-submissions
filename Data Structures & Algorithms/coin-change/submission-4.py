class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(i):
            if i < 0:
                return -1
            if i ==0:
                return 0
            if i in dp:
                return dp[i]

            res = float('inf')
            for c in coins:
                answer = dfs(i-c)
                if answer != -1 and answer < res:
                    res = answer
            if res != float('inf'):
                dp[i] = res + 1
                return res + 1
            else:
                dp[i] = -1
                return -1
        
        return dfs(amount)

        

        