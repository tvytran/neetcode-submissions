class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1

        answer = []

        m = (l+r)//2
        while l <= r:
            if nums[m] == target:
                if m-1 < 0 or nums[m-1] != target:
                    answer.append(m)
                    break
                else:
                    r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
            m = (l+r)//2
        if len(answer) == 0:
            return [-1,-1]
        l = answer[0] 
        r = len(nums) -1
        m = (l+r)//2
        while l <= r:
            if nums[m] == target:
                if m+1 >= len(nums) or nums[m+1] != target:
                    answer.append(m)
                    break
                else:
                    l = m+1
            elif nums[m] < target:
                l = m+1
            else:
                r=m-1
            m = (l+r)//2
        return answer 
        