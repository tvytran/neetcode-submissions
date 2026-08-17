class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        count = 0 
        s = 0
        for n in nums:
            s += n
            if s-k in dic:
                count += dic[s-k]
            if s not in dic:
                dic[s] = 0
            dic[s] +=1
        return count
        