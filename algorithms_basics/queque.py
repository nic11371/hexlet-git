def stack(string):
    intermediate = []
    for i in string:
        if i == "#" and len(intermediate) > 0:
            intermediate.pop()
        elif i != '#':
            intermediate.append(i)
    return "".join(intermediate)


def solution(str1, str2):
    return stack(str1) == stack(str2)


print(solution('ab#c', 'ab#c')) # True
print(solution('ab##', 'c#d#')) # True
print(solution('a#c', 'b')) # False
print(solution('#abc', 'ab#c')) # False
print(solution('a#b#c', 'ab##c#')) # False
print(solution('y#fo##f', 'y#f#o##f')) # True
# print(stack('qwerty##qwerty'))