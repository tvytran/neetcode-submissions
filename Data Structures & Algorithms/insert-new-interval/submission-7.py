class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #heapq.heapify(intervals)
        #heapq.heafppush(intervals, newInterval)

        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
            
        inserted = False

        results = []
        curr = intervals[0]
        for i in range(1,len(intervals)):
            #print("i", i)
            if inserted == False:
                if curr[0] > newInterval[1]:
                    results.append(newInterval)
                    inserted = True
                
                elif curr[1] >= newInterval[0] and curr[1] <= newInterval[1] or newInterval[1] >= curr[0] and newInterval[1] <= curr[1]:
                    curr = [min(curr[0], newInterval[0]), max(curr[1], newInterval[1])]
                    inserted = True
            

        
            other = intervals[i]
            if curr[1] >= other[0] and curr[1] <=other[1] or other[1] >= curr[0] and other[1] <= curr[1]:
                curr = [min(curr[0], other[0]), max(curr[1], other[1])]
            else:
                results.append(curr)
                curr = other


        if inserted == False:
                if curr[0] > newInterval[1]:
                    results.append(newInterval)
                    inserted = True
                
                elif curr[1] >= newInterval[0] and curr[1] <= newInterval[1] or newInterval[1] >= curr[0] and newInterval[1] <= curr[1]:
                    curr = [min(curr[0], newInterval[0]), max(curr[1], newInterval[1])]
                    inserted = True

                         
        results.append(curr)

        if inserted == False:
            results.append(newInterval)

        return results


        