

class Hashtable:
    def __init__(self, size):
        self.table = [None] * size
        self.num_elements = 0
        self.desired_alpha = 0.7

    def hash(self, key):
        return len(key) % len(self.table)

    def resize(self):
        print('Resizing...')
        print(self.table)
        old_array = self.table
        self.table = [None] * (2 * len(old_array))
        self.num_elements = 0

        ## Use hash to put everything in new places
        for item in old_array:
            print(f'Putting item into new table: {item}')
            if item is not None:
                self.put(item[0], item[1])

        print(self.table)

    def put(self, key, value):
        start_location = self.hash(key)
        loc = self.hash(key)
        if self.table[loc] == None:
            print(f'Trying to put {key} in location index {loc}')
            self.table[loc] = (key, value)
        else:
            while self.table[loc] is not None:
                loc += 1
                if loc >= len(self.table):
                    loc = 0
                if loc == start_location:
                    print(f'Checked all locations, did not find an empty one')
                    return
            print(f'Trying to put {key} in location index {loc}')
            self.table[loc] = (key, value)

        self.num_elements += 1
        alpha = self.num_elements / len(self.table)
        if alpha > self.desired_alpha:
            self.resize()


    def get(self, key):
        start_loc = self.hash(key)
        loc = self.hash(key)

        if (self.table[loc][0] == key):
            return self.table[loc]
        else:
            loc += 1
            while (self.table[loc][0] != key):  ## and table[loc] is not None:
                loc += 1
                if loc >= len(self.table):
                    loc = 0
                if loc == start_loc:
                    print(f'Checked all locations, did not find the key')
                    return None
            return self.table[loc]


hashtable = Hashtable(10)
hashtable.put('onion', 3)
hashtable.put('tomato', 4)
hashtable.put('red pepper', 15)
hashtable.put('value', 10)
hashtable.put('queen', 11)
hashtable.put('aster', 12)
print(hashtable.table)
hashtable.put('plaid', 13)
hashtable.put('bonus', 14)

hashtable.put('apple', 42)
hashtable.put('thyme', 56)

hashtable.put('rosemary', 19)

print(hashtable.table)