class Trie:
    def __init__(self):
        self.dic = {}
        self.endOfWord = False
  
class PrefixTree:

    def __init__(self):
        self.start = Trie()    

    def insert(self, word: str) -> None:
        s = self.start
        for c in word:
            if c not in s.dic:
                s.dic[c] = Trie()
            s = s.dic[c]
        s.endOfWord = True

    def search(self, word: str) -> bool:
        s = self.start
        for c in word:
            if c not in s.dic:
                return False
            s = s.dic[c]
        return s.endOfWord

    def startsWith(self, prefix: str) -> bool:
        s = self.start
        for c in prefix:
            if c not in s.dic:
                return False
            s = s.dic[c]
        return True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COL = len(board[0])
        tri = PrefixTree()

        for word in words:
            tri.insert(word)
        
        results = set()
        visit = set()
        def dfs(i,j,sofar):
            if (i,j) in visit or tri.startsWith(sofar) == False:
                return 
            if tri.search(sofar):
                results.add(sofar)
            visit.add((i,j))
            if i+1 < ROWS:
                dfs(i+1, j, sofar + board[i+1][j])
            if i-1 > -1:
                dfs(i-1, j, sofar+ board[i-1][j])
            if j+1 < COL:
                dfs(i, j+1, sofar + board[i][j+1])
            if j -1 > -1:
                dfs(i, j-1, sofar + board[i][j-1])
            visit.remove((i,j))
            return
           #another = sofar + board[i][j]
            

            
        for i in range(ROWS):
            for j in range(COL):
                dfs(i,j, board[i][j])
        
        return list(results)
            

        