class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 
                    'L':0, 'M':0, 'N':0, 'O':0, 'P':0,  'Q':0, 'R':0, 'S':0,'T':0, 'U':0, 'V':0,
                    'W':0, 'X':0,'Y':0,'Z':0 }
        l, r = 0, 0
        maxWin = 0
        while r < len(s):
            letters[s[r]] +=1

            while r-l+1 - max(letters.values())> k:
                letters[s[l]] -=1
                l +=1

            maxWin = max(maxWin, r-l+1)
            r+=1
        return maxWin


            
               