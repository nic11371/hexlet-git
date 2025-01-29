from polymorfizm.Adapter_pattern.passgen import generate_password


# BEGIN (write your solution here)
class PasswordGeneratorAdapter:
    def generate_password(self, length, option):
        return generate_password(length, *option)
# END
