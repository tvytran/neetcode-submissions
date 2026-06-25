class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            length = len(s)
            output += str(length) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
    
        index = 0
        while index < len(s):
            number = ""
            while s[index] != "#":
                number += s[index]
                index +=1
            number = int(number)
            result = ""
            for i in range(index+1, index+number+1):
                result += s[i]
            output.append(result)
            index += number + 1

        return output

