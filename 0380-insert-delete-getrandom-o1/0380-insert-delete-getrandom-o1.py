class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.lis = []

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.dic[val] = len(self.lis)
            self.lis.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            # swap the last element into the position of the element we want to delete
            # then delete the last element instead so we don't have to re-index
            self.lis[self.dic[val]] = self.lis[len(self.lis) - 1]
            self.dic[self.lis[len(self.lis) - 1]] = self.dic[val]
            del self.lis[len(self.lis) - 1]
            del self.dic[val]
            return True
        else:
            return False

    def getRandom(self) -> int:        
        return self.lis[random.randint(0, len(self.lis)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()