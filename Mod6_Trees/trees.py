

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


def traverse(tree):
    if tree is None:
        return
    print(tree)
    traverse(tree.left)
    traverse(tree.right)

def traverse_iterative(tree): ## DFS
    stack = []
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        print(node) ## Visit the node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def traverse_bfs(tree):
    queue = []
    queue.append(tree)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


#### 1 - 2 - 3 - 4 - 5 - 6




joe = Tree('Joe')
jane = Tree('Jane')
dan = Tree('Dan')
sadie = Tree('Sadie')
stella = Tree('Stella')
thomas = Tree('Thomas')

joe.left = jane
joe.right = dan
jane.left = sadie
jane.right = stella
dan.left = thomas

traverse(joe)

print('\n\n\n----')

traverse_iterative(joe)
print('\n\n\n----')

traverse_bfs(joe)
