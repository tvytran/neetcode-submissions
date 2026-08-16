class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            compare = [0] * 26
            for char in s:
                subtract = ord(char) - ord('a')
                compare[subtract] += 1
            turn = tuple(compare)
            if turn not in dic:
                dic[turn] = []
            dic[turn].append(s)
        
        results = []

        for x,y in dic.items():
            output = []
            for each in y:
                output.append(each)
            results.append(output)
        return results

        