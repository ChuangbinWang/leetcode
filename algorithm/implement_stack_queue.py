class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.stack1:
            self.stack1.append(x)
        else:
            self.stack2.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.stack1:
            while len(self.stack1)!=1:
                self.stack2.append(self.stack1.pop())
            return self.stack1.pop()
        else:
            while len(self.stack2)!=1:
                self.stack1.append(self.stack2.pop())
            return self.stack2.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.stack1:
            while len(self.stack1)>0:
                front = self.stack1.pop()
                self.stack2.append(front)
            return front
        else:
            while len(self.stack2)>0:
                front = self.stack2.pop()
                self.stack1.append(front)
            return front
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.stack1 or self.stack2:
            return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()