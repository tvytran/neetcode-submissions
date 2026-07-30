class TimeMap:

    def __init__(self):
        self.emotion = {}
        self.numbers = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.emotion:
            self.emotion[key] = {}
        self.emotion[key][timestamp] = value
        if key not in self.numbers:
            self.numbers[key] = []
        self.numbers[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.numbers:
            return ""
        nums = self.numbers[key]
        length = len(nums)
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r)//2
            curr = nums[m]
            currup = nums[m+1] if m+1 < length else 0
            #print("m",m)

            if m >= length-1:
                if curr <= timestamp:
                    return self.emotion[key][curr]
                break
            elif curr == timestamp or curr < timestamp and currup > timestamp :
                return self.emotion[key][curr]
            elif curr < timestamp and currup <= timestamp:
                l = m+1
            elif curr > timestamp and currup >= timestamp:
                r = m-1
            
        return ""