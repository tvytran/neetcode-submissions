class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        def isPal(l,r):
            while l > -1 and r < len(s):
                #print(s[l:r+1])
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    return s[l+1: r]
            return s[l+1:r]
        
        for i in range(len(s)):
            #odd
            odd = isPal(i,i)
            even = ""

            if i < len(s)-1 and s[i] == s[i+1]:
                even = isPal(i,i+1)
            

            
            oddL = len(odd)
            evenL = len(even)
            resultL = len(result)
            #greater = ""

            if oddL > evenL:
                greater = odd
            else:
                greater = even

            if len(greater) > resultL:
                result = greater
        return result




            


        