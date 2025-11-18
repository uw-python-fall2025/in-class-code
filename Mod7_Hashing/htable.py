

table = [None] * 10
num_elements = 0
desired_alpha = 0.7

def hash(key):
    return len(key) % len(table) ## Lazy!!!

def resize():
    global table
    print('Resizing...')
    old_array = table
    table = [None] * (2 * len(old_array))

    ## Use hash to put everything in new places
    for item in old_array:
        print(f'Putting item into new table: {item}')
        if item is not None:
            table[hash(item[0])] = item

    pass

## Open-Addressing
def put(key, value):
    global num_elements
    start_loc = hash(key)
    loc = hash(key)
    if (table[loc] is None):
        print(f'Trying to put {key} in location index {loc}')
        table[loc] = (key, value)
    else:
        while table[loc] is not None:
            loc += 1
            if loc >= len(table):
                loc = 0
            if loc == start_loc:
                print(f'Checked all locations, did not find an empty one')
                return
        print(f'Trying to put {key} in location index {loc}')
        table[loc] = (key, value)
    num_elements += 1
    alpha = num_elements / len(table)
    if alpha > desired_alpha:
        resize()



def get(key):
    start_loc = hash(key)
    loc = hash(key)

    if (table[loc][0] == key):
        return table[loc]
    else:
        loc += 1
        while (table[loc][0] != key): ## and table[loc] is not None:
            loc += 1
            if loc >= len(table):
                loc = 0
            if loc == start_loc:
                print(f'Checked all locations, did not find the key')
                return None
        return table[loc]


put('onion', 3)
put('tomato', 4)
put('red pepper', 15)
put('value', 10)
put('queen', 11)
put('aster', 12)
print(table)
put('plaid', 13)
put('bonus', 14)

put('apple', 42)
put('thyme', 56)

put('rosemary', 19)

print(table)

print(f"value for onion: {get('onion')}")