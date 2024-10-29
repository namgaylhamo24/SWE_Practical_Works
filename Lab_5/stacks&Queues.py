## Part 1: Implementing a Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2

## Part 2: Implementing a Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2

## Problem 1: Balanced Parentheses
def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False

##Problem 2: Reverse a String
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"

## Problem 3: Hot Potato Simulation
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7))  # The winner's name will be printed

## Exercises for Students:
## Implement a function that uses a stack to evaluate postfix expressions.
def evaluate_postfix(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    for char in expression.split():
        if char not in operators:
            # If it's an operand, push it onto the stack
            stack.push(int(char))
        else:
            # If it's an operator, pop the last two operands and apply the operator
            oprnd2 = stack.pop()
            oprnd1 = stack.pop()
            if char == '+':
                stack.push(oprnd1 + oprnd2)
            elif char == '-':
                stack.push(oprnd1 - oprnd2)
            elif char == '*':
                stack.push(oprnd1 * oprnd2)
            elif char == '/':
                stack.push(oprnd1 / oprnd2)

    return stack.pop()

# Test the function
print(evaluate_postfix("3 4 +"))      # Should print 7
print(evaluate_postfix("10 2 8 * + 3 -"))  # Should print 23

## Ex: B
## 