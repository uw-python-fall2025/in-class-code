
queue = []

def enqueue(queue, new_item):
    queue.append(new_item)

def dequeue(queue):
    return queue.pop(0)

def front(queue):
    return queue[0]

def rear(queue):
    return queue[-1]

enqueue(queue, 'Bob')
enqueue(queue, 'Charlie')
enqueue(queue, 'Big Mac')

print(queue)
print(front(queue))
print(rear(queue))

print(f'The next customer is {dequeue(queue)}')
print(queue)



