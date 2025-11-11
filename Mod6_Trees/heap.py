
class Heap: ## MinHeap
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        cur_ind = len(self.heap) - 1
        parent = cur_ind // 2

        while self.heap[cur_ind] < self.heap[parent]:
            tmp = self.heap[parent]
            self.heap[parent] = data
            self.heap[cur_ind] = tmp
            cur_ind = parent
            parent = cur_ind // 2

    def remove(self):
        root = self.heap[0]

        self.heap[0] = self.heap.pop()
        cur_ind = 0
        left_child_ind = 2 * cur_ind + 1
        right_child_ind = 2 * cur_ind + 2

        ## TODO: Make sure we're not off the end of the heap

        smallest_child_ind = left_child_ind if self.heap[left_child_ind] < self.heap[right_child_ind] else right_child_ind
        print(f'Smallest child is at index {smallest_child_ind}')

        ## Case: At least one child is more important
        while self.heap[cur_ind] > self.heap[smallest_child_ind]:
            print(f'Swapping node {self.heap[cur_ind]} with child at index {smallest_child_ind}')
            tmp = self.heap[cur_ind]
            self.heap[cur_ind] = self.heap[smallest_child_ind]
            self.heap[smallest_child_ind] = tmp

            cur_ind = smallest_child_ind
            left_child_ind = 2 * cur_ind + 1
            right_child_ind = 2 * cur_ind + 2

            if left_child_ind > len(self.heap):
                break
            if right_child_ind > len(self.heap):
                smallest_child_ind = left_child_ind
            else:
                smallest_child_ind = left_child_ind if self.heap[left_child_ind] < self.heap[
                    right_child_ind] else right_child_ind

        return root

    def __repr__(self):
        return str(self.heap)

    def __str__(self):
        return str(self.heap)


heap = Heap()
heap.insert(11)
heap.insert(10)
heap.insert(3)
heap.insert(15)
heap.insert(9)
heap.insert(25)
heap.insert(5)
heap.insert(16)
heap.insert(19)
heap.insert(17)

print(heap)

most_important = heap.remove()
print(most_important)
print(heap)