def solution(book, name):
    if not book:
        return "Phonebook is empty!"

    first = 0
    last = len(book) - 1

    while first <= last:
        avg = (first + last) // 2
        if name == book[avg]['name']:
            return book[avg]['number']
        if name < book[avg]['name']:
            last = avg - 1
        else:
            first = avg + 1
    return 'Name not found!'


phonebook = [
  {'name': 'Alex Bowman', 'number': '48-2002'},
  {'name': 'Aric Almirola', 'number': '10-1001'},
  {'name': 'Bubba Wallace', 'number': '23-1111'},
]

print(solution(phonebook, 'Aric Almirola'))  # '48-2002'
print(solution(phonebook, 'None'))  # 'Name not found!'
print(solution([], 'Alex Bowman'))  # 'Phonebook is empty!'
