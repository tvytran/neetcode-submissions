class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.condition = {}

    def get(self, key: int) -> int:
        if key in self.condition:
            value = self.condition.pop(key)
            self.condition[key] = value
            return value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.condition) == self.cap:
            if key in self.condition:
                self.condition.pop(key)
            else:
                for k,v in self.condition.items():
                    self.condition.pop(k)
                    break
        self.condition[key] = value
        
        
