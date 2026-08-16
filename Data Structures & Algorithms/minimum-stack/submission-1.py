class MinStack:

    def __init__(self):
        self.curr = []
        self.minn = []

        

    def push(self, val: int) -> None:
        self.curr.append(val)
        if len(self.minn) > 0:
            old = self.minn[-1]
            if old > val:
                self.minn.append(val)
            else:
                self.minn.append(old)
        else:
            self.minn.append(val)
        

    def pop(self) -> None:
        self.curr.pop()
        self.minn.pop()
        

    def top(self) -> int:
        return self.curr[-1]
        

    def getMin(self) -> int:
        return self.minn[-1]
        
