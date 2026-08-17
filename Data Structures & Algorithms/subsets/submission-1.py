import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        visit = set()

        def dfs(i, res):
            if i == len(nums):
                dup = copy.deepcopy(res)
                solution.append(dup)
                return
            
            
            res.append(nums[i])
            dfs(i+1, res)
            res.pop()
            dfs(i+1, res)
            return
        
        dfs(0, [])
        return solution 