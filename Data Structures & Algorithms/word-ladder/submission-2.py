class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashMap = {}
        length = len(wordList[0])

        for word in wordList:
            for i in range(length):
                prev = word[0:i]
                after = word[i+1:]

                part = prev + "*" + after

                if part not in hashMap:
                    hashMap[part] = []
                hashMap[part].append(word)

        visited = set()
        neighbors = deque()
        neighbors.append((1,beginWord))
        print("neighbors", neighbors)
        while neighbors:
            print("neighbors", neighbors)
            size, word = neighbors.popleft()
            visited.add(word)

            if word == endWord:
                return size

            for i in range(length):
                prev = word[0:i]
                after = word[i+1:]

                part = prev + "*" + after
                
                if part in hashMap and part not in visited:
                    for each in hashMap[part]:
                        if each not in visited:
                            neighbors.append((size+1, each))
                    visited.add(part)
        return 0
                
                        