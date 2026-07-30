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
            #print('hello')
            return ""
        nums = self.numbers[key]
        #print(nums)
        l = 0
        r = len(nums)-1
        #print(self.emotion)
        #print(self.numbers)

        while l <= r:
            m = (l+r)//2
            print("m",m)

            if m >= len(nums)-1:
                if nums[m] <= timestamp:
                    return self.emotion[key][nums[m]]
                break
            elif nums[m] == timestamp or nums[m] < timestamp and nums[m+1] > timestamp :
                return self.emotion[key][nums[m]]
            elif nums[m] < timestamp and nums[m+1] <= timestamp:
                l = m+1
            elif nums[m] > timestamp and nums[m+1] >= timestamp:
                r = m-1
            
        return ""