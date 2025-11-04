def create_ll_node(payload):
    return {
        'data': payload,
        'next': None,
        'prev': None
    }


def create_ll():
    return {'head': None,
            'tail': None,
            'length': 0 }


def insert_tail(ll, ll_node):
    if ll['head'] is None:  ## Nothing in the list
        ll['head'] = ll_node
        ll['tail'] = ll_node
        ll['length'] = 1
        return
    ## Tell the tail that the new thing is next
    ll['tail']['next'] = ll_node
    ## Tell the new thing that the prev thing is the tail
    ll_node['prev'] = ll['tail']
    ## Tell the list that the new thing is now the tail
    ll['tail'] = ll_node
    ll['length'] += 1

def is_palindrome(ll):
    left_elem = ll['head']
    right_elem = ll['tail']
    counter = 0 ## Number of pairs we've compared

    while counter < ll['length']/2:
        if left_elem['data'] == right_elem['data']:
            counter += 1
            left_elem = left_elem['next']
            right_elem = right_elem['prev']
        else:
            return False

    return True


    pass

def print_node(ll_node):
    data_name = ll_node['next']['data'] if ll_node['next'] else "Nothing"
    print(f'Data: {ll_node['data']}; Next: {data_name}')


def print_list(ll_list):
    print('----')
    node = ll_list['head']
    while node is not None:
        print_node(node)
        node = node['next']
    print(f'List has {ll_list['length']} elements')
    print('----')


my_list = create_ll()

insert_tail(my_list, create_ll_node('t'))
insert_tail(my_list, create_ll_node('a'))
insert_tail(my_list, create_ll_node('c'))

insert_tail(my_list, create_ll_node('c'))
insert_tail(my_list, create_ll_node('a'))
insert_tail(my_list, create_ll_node('t'))
insert_tail(my_list, create_ll_node('t'))

print_list(my_list)

print(is_palindrome(my_list))