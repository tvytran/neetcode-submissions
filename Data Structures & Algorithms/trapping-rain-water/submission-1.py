class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        total = 0
        lwall = heights[l]
        rwall = heights[r]

        while l <= r:
            if lwall < rwall:
                lwall = max(heights[l], lwall)
                total += lwall - heights[l]
                l +=1
            else:
                rwall = max(heights[r], rwall)
                total += rwall - heights[r]
                r -=1
        return total