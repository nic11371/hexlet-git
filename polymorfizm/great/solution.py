# BEGIN (write your solution here)
def greet(user):
    name = user.get_name()
    if user.is_guest():
        return "Nice to meet you Guest!"
    elif user.is_user():
        return f"Hello {name}!"
# END
