class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s), -1, -1):
            for w in wordDict:
                if i + len(w) < len(dp):
                    if s[i:i+len(w)] == w and dp[i] == False:
                        dp[i] = dp[i+len(w)]
        print("dp", dp)

        return dp[0]

