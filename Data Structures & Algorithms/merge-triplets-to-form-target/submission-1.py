class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        goal = [False] * len(target)
        first = target[0]
        second = target[1]
        third = target[2]

        for t in triplets:
            one = t[0]
            two = t[1]
            three = t[2]

            if one > first or two > second or three > third:
                continue
            
            if one == first:
                goal[0] = True
            if two == second:
                goal[1] = True
            if three == third: 
                goal[2] = True

        for g in goal:
            if g == False:
                return False
        
        return True
         