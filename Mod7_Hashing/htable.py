

table = [None] * 20

def hash(key):
    return len(key)

## Open-Addressing
def put(key, value):
    loc = hash(key)
    if (table[loc] is None):
        table[loc] = (key, value)
    else:
        while table[loc] is not None:
            loc += 1
        table[loc] = (key, value)



def get(key):
    loc = hash(key)

    if (table[loc][0] == key):
        return table[loc]
    else:
        loc += 1
        while (table[loc][0] != key): ## and table[loc] is not None:
            loc += 1
        return table[loc]


put('onion', 3)
put('tomato', 4)
put('red pepper', 15)

put('apple', 42)

print(table)

print(f"value for onion: {get('onion')}")