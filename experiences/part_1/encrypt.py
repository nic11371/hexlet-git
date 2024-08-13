def encrypt(str):
    string_reverse = ''
    for i in range(0, len(str), 2):
        two = str[i:i+2]
        string_reverse += two[::-1]
    return string_reverse


print(encrypt("move"))  # 'omev'
print(encrypt("attack"))  # 'taatkc'
print(encrypt("go!"))  # 'og!'
