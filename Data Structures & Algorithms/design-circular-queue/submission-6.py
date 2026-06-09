class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.front = 0
        self.rear = 0
        self.array = [0] * k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.array[self.rear%self.size] = value
        self.rear +=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front +=1
        return True       

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.front%self.size]
        
    def Rear(self) -> int:
        print(self.rear)
        print(self.array)
        if self.isEmpty():
            return -1
        return self.array[(self.rear-1)%self.size]
        

    def isEmpty(self) -> bool:
        return self.front == self.rear
        

    def isFull(self) -> bool:
        return self.rear - self.front == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()