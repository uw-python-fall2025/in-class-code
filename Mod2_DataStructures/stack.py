from array import array

stack = array('i')

def push(stack, new_item):
    stack.append(new_item)

def pop(stack):
    return stack.pop()

def peek(stack):
    # return stack[len(stack) - 1]
    return stack[-1]


push(stack, 57)
print(stack)
push(stack, 42)
push(stack, 11)
print(stack)

top_book = pop(stack)
print(top_book)
print(stack)

print(peek(stack))
print(stack)
