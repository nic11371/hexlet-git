from itertools import chain


def get_girl_friends(users):
    friends = map(lambda f: f['friends'], users)
    all_friends = list(chain.from_iterable(friends))
    girl_friends = filter(lambda g: g['gender'] == 'female', all_friends)
    return list(girl_friends)


users = [
    {
        'name': 'Tirion',
        'friends': [
            {'name': 'Mira', 'gender': 'female'},
            {'name': 'Ramsey', 'gender': 'male'},
        ],
    },
    {'name': 'Bronn', 'friends': []},
    {
        'name': 'Sam',
        'friends': [
            {'name': 'Aria', 'gender': 'female'},
            {'name': 'Keit', 'gender': 'female'},
        ],
    },
    {
        'name': 'Rob',
        'friends': [
            {'name': 'Taywin', 'gender': 'male'},
        ],
    },
]

print(get_girl_friends(users))
