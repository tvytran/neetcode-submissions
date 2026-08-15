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
        neighbors = []
        heapq.heapify(neighbors)
        heapq.heappush(neighbors, (1, beginWord))
        while neighbors:

            size, word = heapq.heappop(neighbors)
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
                            heapq.heappush(neighbors, (size+1, each))
                    visited.add(part)
        return 0
                
                        