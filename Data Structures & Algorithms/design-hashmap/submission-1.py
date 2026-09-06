class MyHashMap:

    def __init__(self):
        self.table = []

    def put(self, key: int, value: int) -> None:
        for x in range(len(self.table)):
            if self.table[x][0] == key:
                self.table[x][1] = value
                return
        self.table.append([key,value])

    def get(self, key: int) -> int:
        for x in range(len(self.table)):
            if self.table[x][0] == key:
                return self.table[x][1]
        return -1  

    def remove(self, key: int) -> None:
        for x in range(len(self.table)):
            if self.table[x][0] == key:
                self.table.pop(x)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)