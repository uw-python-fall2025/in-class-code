
min_stack = { elements: [], min_val: []}

def push(elem):
    min_stack.min_val.append(min(elem, min_stack.elements[-1]))
    min_stack.elements.append(elem)

def
