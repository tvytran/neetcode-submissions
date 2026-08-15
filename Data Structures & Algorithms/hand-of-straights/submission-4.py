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
                if hashMap[i] == 0:
                    if minH[0] != i:
                        #print("here")
                        return False
                    heapq.heappop(minH)
        
        return True

                


            
