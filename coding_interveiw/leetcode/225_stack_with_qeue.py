class MyStack:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        got = self.data.pop()
        return got

    def top(self) -> int:
        return self.data[-1]

    def empty(self) -> bool:
        if not self.data:
            return True

        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(10)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()