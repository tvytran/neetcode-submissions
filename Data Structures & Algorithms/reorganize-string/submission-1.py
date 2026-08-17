class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        heapq.heapify(heap)

        count = {}
        for char in s:
            if char not in count:
                count[char] = 0
            count[char] -= 1
        
        for char, amount in count.items():
            heapq.heappush(heap, (amount, char))
        
        queue = deque()
        combination = ""
        while heap or queue:
            if len(heap) == 0 and len(queue) == 1 and len(combination) > 0 and queue[0][1] == combination[-1]:
                return ""
            while queue and queue[0][1] != combination[-1]:
                value = queue.popleft()
                heapq.heappush(heap, value)
            
            value = heapq.heappop(heap)
            combination += value[1]
            if value[0] + 1 != 0:
                queue.append((value[0]+1, value[1]))

        return combination
            