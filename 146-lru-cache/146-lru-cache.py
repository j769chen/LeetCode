class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.queue = deque()

    def get(self, key: int) -> int:
        if key in self.dic:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dic[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            self.dic[key] = value
            self.queue.append(key)
            if len(self.queue) > self.capacity:
                temp = self.queue.popleft()
                self.dic.pop(temp, None)
                
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)