def create_ll_node(payload):
    return {
        'data': payload,
        'next': None
    }


def create_ll():
    return {'head': None}


def insert(ll, ll_node):
    if ll['head'] is None:  ## Nothing in the list
        ll['head'] = ll_node
        return
    node = ll['head']
    while node['next'] is not None:
        node = node['next']
    node['next'] = ll_node

def insert_head(ll, ll_node):
    ll_node['next'] = ll['head']
    ll['head'] = ll_node

def delete(ll, node_data):
    if ll['head'] is None:
        return
    cur_node = ll['head']
    if cur_node['data'] == node_data:
        ll['head'] = cur_node['next']
    while cur_node['next']['data'] != node_data:
        cur_node = cur_node['next']
        if cur_node['next'] is None:
            return ## Couldn't find the data
    node_to_delete = cur_node['next']
    cur_node['next'] = node_to_delete['next']
    return node_to_delete





def print_node(ll_node):
    data_name = ll_node['next']['data'] if ll_node['next'] else "Nothing"
    print(f'Data: {ll_node['data']}; Next: {data_name}')


def print_list(ll_list):
    print('----')
    node = ll_list['head']
    while node is not None:
        print_node(node)
        node = node['next']
    print('----')


my_list = create_ll()
ace_spades = create_ll_node('Ace of Spades')
insert(my_list, ace_spades)

six_clubs = create_ll_node('Six Clubs')
insert(my_list, six_clubs)

two_spades = create_ll_node('Two Spades')
insert(my_list, two_spades)

four_hearts = create_ll_node('Four Hearts')
insert(my_list, four_hearts)

nine_clubs = create_ll_node('Nine Clubs')
insert(my_list, nine_clubs)

# print_node(six_clubs)

print_list(my_list)

delete(my_list, 'Four Hearts')
delete(my_list, 'Four Hearts')
delete(my_list, 'Ace of Spades')
# delete(my_list, 'Nine Clubs')

print_list(my_list)
