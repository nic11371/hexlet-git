opening_symbols = ['(', '[', '{', '<']
closing_symbols = [')', ']', '}', '>']


# BEGIN (write your solution here)
def get_opening_symbols(symbol):
    if symbol in opening_symbols:
        return closing_symbols[opening_symbols.index(symbol)]
    return None


def are_symbols_balanced(string):
    stack = []
    for i in string:
        if i in opening_symbols:
            close_index = get_opening_symbols(i)
            stack.append(close_index)
        else:
            if not stack:
                return False
            last_symbol = stack.pop()
            if i != last_symbol:
                return False
    return len(stack) == 0
# END


print(are_symbols_balanced('()'))  # is True
print(are_symbols_balanced('[()]'))  # is True
print(are_symbols_balanced('({}[])'))  # is True
print(are_symbols_balanced('(<><<{[()]}>>)'))  # is True
print(are_symbols_balanced(''))  # is True

print(are_symbols_balanced('(('))  # is False
print(are_symbols_balanced('[[()]'))  # is False
print(are_symbols_balanced('({}}[]'))  # is False
print(are_symbols_balanced('(<><<{[()]}>>>)'))  # is False
print(are_symbols_balanced('}'))  # is False
print(are_symbols_balanced('([)]'))  # is False
print(are_symbols_balanced('([))'))  # is False

print(are_symbols_balanced('()'))  # is True
print(are_symbols_balanced('[()]'))  # is True
print(are_symbols_balanced('({}[])'))  # is True
print(are_symbols_balanced('(<><<{[()]}>>)'))  # is True
print(are_symbols_balanced(''))  # is True
