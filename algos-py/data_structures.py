# Stack, Queue, Deque (LIFO/FIFO/LILO demos)

# STACK ============================================================================================================
# LIFO: Last In First Out

# Basic operations to do on stacks:
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


# QUEUE ============================================================================================================
# FIFO: First In First Out.

# Basic operations to do on queues:
# Enqueue: Adds a new element to the queue.
# Dequeue: Removes and returns the first (front) element from the queue.
# Peek: Returns the first element in the queue.
# isEmpty: Checks if the queue is empty.
# Size: Finds the number of elements in the queue.

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.queue.isEmpty():
            return "queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.queue.isEmpty():
            return "queue is empty"
        return self.queue[0]

    def size(self):
        return len(self.queue)
    
# Creating a queue
queue1 = Queue()

queue1.enqueue('A')
queue1.enqueue('B')
queue1.enqueue('C')
print("Queue: ", queue1.queue)

print("Dequeue: ", queue1.dequeue())

print("Peek: ", queue1.peek())

print("isEmpty: ", queue1.isEmpty())

print("Size: ", queue1.size())