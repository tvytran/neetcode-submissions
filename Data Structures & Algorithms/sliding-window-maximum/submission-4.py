class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        result = []
        
        for i in range(k):
            while len(d) > 0 and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
        result.append(nums[d[0]])

        for i in range(k,len(nums)):
            while len(d) > 0 and nums[d[-1]] < nums[i] :
                d.pop()
            d.append(i)
            while len(d) > 0 and i-k >= d[0]:
                d.popleft()
            result.append(nums[d[0]])
        return result