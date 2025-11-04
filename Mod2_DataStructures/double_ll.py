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


def insert_head(ll, ll_node):
    ## Tell the current head to point back to the new elem
    ll['head']['prev'] = ll_node
    ## Tell the new elem to point forward to the current head
    ll_node['next'] = ll['head']
    ## Make the new elem the new head
    ll['head'] = ll_node

# def delete(ll, node_data):
#     if ll['head'] is None:
#         return
#     cur_node = ll['head']
#     if cur_node['data'] == node_data:
#         ll['head'] = cur_node['next']
#         ll['head']['prev'] = None
#     while cur_node['data'] != node_data:
#         cur_node = cur_node['next']
#         if cur_node['next'] is None:
#             return ## Couldn't find the data
#     node_to_delete = cur_node
#     cur_node['prev']['next'] = node_to_delete['next']
#     if node_to_delete['next'] is None:
#         ## We are deleting the tail of the list
#         ll['tail'] = node_to_delete['prev']
#     else:
#         node_to_delete['next']['prev'] = node_to_delete['prev']
#     return node_to_delete





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
insert_tail(my_list, ace_spades)

six_clubs = create_ll_node('Six Clubs')
insert_tail(my_list, six_clubs)

two_spades = create_ll_node('Two Spades')
insert_tail(my_list, two_spades)

four_hearts = create_ll_node('Four Hearts')
insert_tail(my_list, four_hearts)

nine_clubs = create_ll_node('Nine Clubs')
insert_head(my_list, nine_clubs)

# print_node(six_clubs)

print_list(my_list)

delete(my_list, 'Four Hearts')
# delete(my_list, 'Four Hearts')
# delete(my_list, 'Ace of Spades')
# # delete(my_list, 'Nine Clubs')
#
print_list(my_list)
