class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        minn = prices[0]
        diff = 0

        r = 1
        while r < len(prices):
            if prices[r] < minn:
                minn = prices[r]
            diff = max(diff, prices[r]-minn)
            r+=1
        return diff
