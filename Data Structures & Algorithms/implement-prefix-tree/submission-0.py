class Trie:
    def __init__(self):
        self.dic = {}
        self.endOfWord = False
  
class PrefixTree:

    def __init__(self):
        self.start = Trie()    

    def insert(self, word: str) -> None:
        def dfs(i, n):
            if len(word)==i:
                n.endOfWord = True
                return
            if word[i] not in n.dic:
                n.dic[word[i]] = Trie()
            return dfs(i+1, n.dic[word[i]])
        dfs(0, self.start)

    def search(self, word: str) -> bool:
        def dfs(i,n):
            if len(word) == i:
                return n.endOfWord
            if word[i] not in n.dic:
                return False
            return dfs(i+1, n.dic[word[i]])
        return dfs(0,self.start)

    def startsWith(self, prefix: str) -> bool:
        def dfs(i,n):
            if len(prefix) == i:
                return True
            if prefix[i] not in n.dic:
                return False
            return dfs(i+1, n.dic[prefix[i]])
        return dfs(0, self.start)
        
        
        
        