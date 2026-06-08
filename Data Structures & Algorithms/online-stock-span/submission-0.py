class StockSpanner:

    def __init__(self):
        self.nums = []
        

    def next(self, price: int) -> int:
        self.nums.append(price)
        output = 0
        #print(len(self.nums))
        for i in range(len(self.nums)-1, -1,-1):
            if self.nums[i] <= price:
                output +=1
            else:
                break
        return output
        #print(str(price), ":", str(output))


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)