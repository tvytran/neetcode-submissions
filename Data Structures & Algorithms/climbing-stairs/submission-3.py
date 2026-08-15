class Solution:
    def climbStairs(self, n: int) -> int:
        #fibonacci

        further = 0
        prev = 1

        result = 0
        for i in range(n):
            result = further + prev
            further = prev
            prev = result
        return result


        