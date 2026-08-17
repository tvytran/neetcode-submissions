class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def count(i):
            time = 0
            for p in piles:
                time += p//i
                if p%i > 0:
                    time +=1
            return time
        
        result = high
        mid = (low + high)//2
        while low <= high:
            c = count(mid)
            if c <= h:
                result = min(result, mid)
                high = mid - 1
            elif c > h:
                low = mid+1

            mid = (low+high)//2

        return result

