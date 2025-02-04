from functools import reduce


# def group_by(coll, sign):
#     if not coll:
#         return {}

#     def group_by_sign(acc, coll):
#         if coll[sign] not in acc:
#             acc[coll[sign]] = []
#         acc[coll[sign]].append(coll)
#         return acc
#     return reduce(group_by_sign, coll, {})


def group_by(objects, key):
    def reducer(acc, obj):
        # из каждого объекта берётся значение по ключу
        group_name = obj[key]
        # контейнером группы выступает список
        # метод get возвращает пустой список, если в аккумуляторе ничего нет
        group = acc.get(group_name, [])
        # возвращается новый словарь аккумулятора
        # старый аккумулятор обновляется
        # для текущей группы записывается новый список с данными
        return {**acc, group_name: group + [obj]}

    return reduce(reducer, objects, {})


students = [
    {'name': 'Tirion', 'class': 'B', 'mark': 3},
    {'name': 'Keit', 'class': 'A', 'mark': 3},
    {'name': 'Ramsey', 'class': 'A', 'mark': 4},
]

print(group_by([], ''))  # => {}
print(group_by(students, 'mark'))

# => {
# =>   3: [
# =>     {'name': 'Tirion', 'class': 'B', 'mark': 3},
# =>     {'name': 'Keit', 'class': 'A', 'mark': 3},
# =>   ],
# =>   4: [
# =>     {'name': 'Ramsey', 'class': 'A', 'mark': 4},
# =>   ],
# => }
