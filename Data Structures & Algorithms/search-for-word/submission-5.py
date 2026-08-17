class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        def dfs(i,j, char):
            if (i,j) in visit or i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
                return False
            if board[i][j] == word[char]:
                if char == len(word)-1:
                    return True
                visit.add((i,j))    
                if dfs(i+1, j,char+1) or dfs(i-1,j,char+1) or dfs(i,j+1,char+1) or dfs(i,j-1,char+1):
                    visit.remove((i,j))
                    return True
                else:
                    visit.remove((i,j))
                    return False

            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False

        