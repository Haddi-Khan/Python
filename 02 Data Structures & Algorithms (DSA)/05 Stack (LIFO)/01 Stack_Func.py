stack = []

def push(x):
    stack.append(x)

def pop():
    if not stack:
        print("Stack Underflow")
    else:
        return stack.pop()

def peek():
    if not stack:
        return "Stack is empty"
    return stack[-1]

push(5)
push(15)
push(25)
print(pop())
print(peek())
