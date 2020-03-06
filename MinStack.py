'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = []

    def push(self, x: int) -> None:
        self.items.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        if not self.items:
            return None
        item = self.items.pop()
        if item == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        if not self.items:
            return None
        return self.items[-1]
        

    def getMin(self) -> int:
        if not self.min:
            return None
        return self.min[-1]



if __name__ == '__main__':

    minStack = MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);   
    print(minStack.getMin());          #Returns -3
    minStack.pop();
    print(minStack.top());                    #Returns 0
    print(minStack.getMin());          #Returns -2
    
