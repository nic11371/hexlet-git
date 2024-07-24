def get_first_name(str):
    person = str.split('_')
    name, last_name = person
    return name


def sort_by(func, names):
    names_copy = names[:]
    return sorted(names_copy, key=func)


users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

print(get_first_name("Vader_Darth"))
print(sort_by(get_first_name, users))
print(users)
