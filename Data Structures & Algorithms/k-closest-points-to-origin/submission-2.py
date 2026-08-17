class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = {}
        priority  = []
        heapq.heapify(priority)

        for p in points:
            distance = math.sqrt((p[0] - 0)**2 + (p[1] - 0) ** 2)
            if distance not in dis:
                heapq.heappush(priority, distance)
                dis[distance] = []
            dis[distance].append(p)
        
        res = []
        amount = 0
        while amount < k:
            value = heapq.heappop(priority)
            for p in dis[value]:
                if amount == k:
                    return res
                res.append(p)
                amount += 1
        
        return res 