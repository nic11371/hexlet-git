def invert_case(str):
    new_str = []
    for i in str:
        if i.islower():
            new_str.append(i.upper())
        else:
            new_str.append(i.lower())
    return "".join(new_str)


print(invert_case('Hello, World!'))
