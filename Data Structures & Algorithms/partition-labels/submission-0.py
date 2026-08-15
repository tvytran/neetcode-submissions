class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        results = []

        l = 0
        r = 0

        hashMap = {}
        for i in range(len(s)):
            hashMap[s[i]]= i
        
        for i in range(len(s)):
            if hashMap[s[i]] > r:
                r = hashMap[s[i]]
            if i == r:
                results.append(r-l+1)
                l = i+1
                r= -1
        return results
            