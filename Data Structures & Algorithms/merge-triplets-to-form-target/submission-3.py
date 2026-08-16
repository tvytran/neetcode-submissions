class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        goal = set()
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
                goal.add(1)
            if two == second:
                goal.add(2)
            if three == third: 
                goal.add(3)

        
        return len(goal) == 3
         