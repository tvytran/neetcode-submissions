class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            if t not in count:
                count[t] = 0
            count[t] -=1
        
        here = list(count.values())
        heapq.heapify(here)
        #print(here)

        
        res = 0
        total = len(here)
        queue = deque()

        while queue or here:
            res +=1
            if not here: 
                res = queue[0][1]
            else:
                value = heapq.heappop(here)
                if value+1 < 0:
                    queue.append((value+1,  res + n ))
            while queue and queue[0][1] <= res:
                heapq.heappush(here, queue[0][0])
                queue.popleft()

        return res





         