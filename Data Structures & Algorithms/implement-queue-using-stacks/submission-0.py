class MyQueue:

    def __init__(self):
        self.fifa = deque()

    def push(self, x: int) -> None:
        self.fifa.append(x)

    def pop(self) -> int:
        return self.fifa.popleft()

    def peek(self) -> int:
        return self.fifa[0]

    def empty(self) -> bool:
        return not self.fifa


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()