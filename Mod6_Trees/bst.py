class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)
        # return f'{str(self.data)}: Left: {self.left}, Right: {self.right}'

def traverse(tree):
    if tree is None:
        return
    print(tree)
    traverse(tree.left)
    traverse(tree.right)

def traverse_depth(tree, level = 0):
    if tree is None:
        return
    for i in range(1, level + 1):
        print('-', end='')
    print(tree)
    traverse_depth(tree.left, level + 1)
    traverse_depth(tree.right, level + 1)




def insert(root, data):
    if not root:
        root = Tree(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)

    return root

def search(root, data):
    print(f'Checking for data {data} in node {root.data}')
    if not root:
        return None
    if root.data == data:
        print('Found it!')
        return root
    if data < root.data:
        print('Looking in the left child')
        return search(root.left, data)
    else:
        print('Looking in the right child')
        return search(root.right, data)


tree = insert(None, 25)
tree = insert(tree, 15)
tree = insert(tree, 52)
tree = insert(tree, 5)
tree = insert(tree, 17)
tree = insert(tree, 38)
tree = insert(tree, 100)

traverse_depth(tree)

search(tree, 38)


print('\n\n\n----')
tree2 = insert(None, 5)
tree2 = insert(tree2, 15)
tree2 = insert(tree2, 17)
tree2 = insert(tree2, 25)
tree2 = insert(tree2, 38)
tree2 = insert(tree2, 52)
tree2 = insert(tree2, 100)


search(tree2, 38)





traverse_depth(tree2)