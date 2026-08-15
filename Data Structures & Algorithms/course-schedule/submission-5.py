class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        for a,b in prerequisites:
            if a not in dic:
                dic[a] = []
            dic[a].append(b)
        
        visited = set()
        def dfs( i):
            if i not in dic or len(dic[i]) == 0:
                return True
            if i in visited:
                return False
            
            visited.add(i)
            for c in dic[i]:
                if dfs(c) == False:
                    return False
            visited.remove(i)
            dic[i]=[]
            return True
        for course, pre in dic.items():
            if dfs(course) == False:
                return False
        return True

         


        
        