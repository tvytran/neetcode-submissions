class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False

        hashMap = {}
        for h in hand:
            if h not in hashMap:
                hashMap[h] = 0
            hashMap[h] +=1

        minH = list(hashMap.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first+groupSize):
                if i not in hashMap:
                    return False
                hashMap[i] -= 1
                if hashMap[i] == 0 and minH[0] != i:
                    return False
                elif hashMap[i] == 0: 
                    heapq.heappop(minH)
        
        return True

                


            
