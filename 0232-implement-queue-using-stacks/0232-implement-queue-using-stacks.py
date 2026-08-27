class MyQueue:

    def __init__(self):
        self.set1=[]
        self.set2=[]

    def push(self, x: int) -> None:
        while self.set1:
            self.set2.append(self.set1.pop())
        self.set1.append(x)
        while self.set2:
            self.set1.append(self.set2.pop())


    def pop(self) -> int:
        return self.set1.pop()

    def peek(self) -> int:
        return self.set1[-1]

    def empty(self) -> bool:
        return len(self.set1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()