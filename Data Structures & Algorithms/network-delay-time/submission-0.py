class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dic = {}
        results = {}

        for i in range(n):
            results[i+1] = -1
        results[k] = 0
        for t in times:
            ui = t[0]
            vi = t[1]
            ti = t[2]

            if ui not in dic:
                dic[ui] = []
            dic[ui].append((ti, vi))

        
        visit = set()
        minHeap = [(0,k)]
        t = 0

        while minHeap:
            t1, p = heapq.heappop(minHeap)
            if p in visit:
                continue
            visit.add(p)
            t = max(t, t1)

            if p in dic:
                for time, val in dic[p]:
                    heapq.heappush(minHeap, (t + time, val))

        return t if len(visit) == n else -1
            

                


