# Stack, Queue, Deque (LIFO/FIFO/LILO demos)

# STACKS ============================================================================================================
# Push: Adds a new element on the stack.
# Pop: Removes and returns the top element from the stack.
# Peek: Returns the top (last) element on the stack.
# isEmpty: Checks if the stack is empty.
# Size: Finds the number of elements in the stack.

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
# Creating a stack:
stack1 = Stack()

stack1.push("fig1")
stack1.push("fig2")
stack1.push("fig3")

print("Stack: ", stack1.stack)
print("Pop: ", stack1.pop())
print("Stack after Pop: ", stack1.stack)
print("Peek: ", stack1.peek())
print("isEmpty: ", stack1.isEmpty())
print("Size: ", stack1.size())