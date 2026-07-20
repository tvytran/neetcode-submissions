class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(heights[0],0)]
        results = []
        #print("stack = ", stack)

        for i in range(1,len(heights)):
           # print("i = ", i)
            #print("results = ", results)
           # print("stack = ", stack)
            left = 0
            minh = float('inf')
            while len(stack) > 0 and stack[-1][0] > heights[i]:
                height = stack.pop()
                if len(stack) == 0:
                    results.append(height[0]*(i))
                else:
                    results.append(height[0] * (i - stack[-1][1] - 1))
            stack.append((heights[i], i) )
            
        while len(stack) > 0:
            height = stack.pop()
            if len(stack) == 0:
                results.append(height[0]*(len(heights)))
            else:
                results.append(height[0] * (len(heights) - stack[-1][1]-1))
            #print("results = ", results)

        return max(results)