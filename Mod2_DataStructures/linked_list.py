
def create_ll_node(data):
    return { 'data': data,
             'next': None }

def create_ll():
    return { 'head': None }

def insert(ll, ll_node):
    if ll['head'] is None: ## Nothing in the list
        ll['head'] = ll_node
        return
    node = ll['head']
    while node['next'] is not None:
        # print_node(node)
        node = node['next']
    node['next'] = ll_node

    #     if node['next'] is None: ## It's the last node in the list
    #     node['next'] = ll_node

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

# print_node(six_clubs)

print_list(my_list)



