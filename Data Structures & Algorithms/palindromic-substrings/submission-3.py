class Solution:
    def countSubstrings(self, s: str) -> int:
        results = []
        for i in range(len(s)):

            l,r = i,i 
            while l > -1 and r < len(s) and s[l] == s[r]:
                results.append(s[l:r+1])
                l-=1
                r+=1
            if i+1 <len(s):
                l,r = i, i+1
                while l > -1 and r < len(s) and s[l] == s[r]:
                    results.append(s[l:r+1])
                    l-=1
                    r+=1
        #print(results)
        return len(results)