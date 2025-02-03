from itertools import chain


# BEGIN (write your solution here)
def get_children(users):
    children = map(lambda c: c['children'], users)
    return list(chain.from_iterable(children))
# END


users = [
    {
        'name': 'Tirion',
        'children': [
            {'name': 'Mira', 'birthday': '1983-03-23'},
        ],
    },
    {'name': 'Bronn', 'children': []},
    {
        'name': 'Sam',
        'children': [
            {'name': 'Aria', 'birthday': '2012-11-03'},
            {'name': 'Keit', 'birthday': '1933-05-14'},
        ],
    },
    {
        'name': 'Rob',
        'children': [
            {'name': 'Tisha', 'birthday': '2012-11-03'},
        ],
    },
]

# def get_children(users):
#     def extract_children(user):
#         return user.get('children', [])

#     children_of_users = map(extract_children, users)
#     return list(chain.from_iterable(children_of_users))
# # END


print(get_children(users))
