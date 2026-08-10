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