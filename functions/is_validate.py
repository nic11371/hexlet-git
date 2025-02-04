def validate_passwords(password):
    length = any(p for p in password if len(p) >= 8)
    integer = any(not p.isdigit() for p in password)
    capital = any(p.istitle() for p in password)
    space = any(not p.isspace() for p in password)
    return all([length, integer, capital, space])


# def validate_passwords(passwords):
#     return all((
#         all(len(password) >= 8 for password in passwords),

#         any(any(char.isdigit() for char in password) for password in passwords),

#         any(any(char.isupper() for char in password) for password in passwords),

#         all(' ' not in password for password in passwords)
#     ))


print(validate_passwords(['short', '1234567']))
print(validate_passwords(['password', 'strongPass']))
print(validate_passwords(['password123', 'strongpass1']))
print(validate_passwords(['password 123', 'strongPass1']))
print(validate_passwords(['password123', 'Password123', 'StrongPass1']))
