class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []

        def dfs(x,y, cols, pos, neg, passed):
            if x == n:
                results.append(passed.split())
                return 
            elif y  in cols or x + y in pos or x-y in neg:
                return

            cols.add(y)
            pos.add(x+y)
            neg.add(x-y)

            pas = ""
            for i in range(n):
                if i == y:
                    pas += "Q"
                else:
                    pas += "."
            pas += " "

            passed += pas 
            row = x+1

            if row == n:
                results.append(passed.split())
            else:
                for j in range(n):
                    dfs(row,j, cols, pos,neg, passed)
                    
            cols.discard(y)
            pos.discard(x+y)
            neg.discard(x-y)
        cols = set()
        pos = set()
        neg = set()
        passed = ""

        for k in range(n):
            dfs(0,k, cols, pos,neg, passed)

        return results