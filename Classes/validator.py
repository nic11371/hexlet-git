class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    # BEGIN (write your solution here)

    def __init__(self, **options):
        self.options = PasswordValidator.OPTIONS | options
        self.errors = {}

    def validate(self, check):
        if self.is_check_length(check):
            self.errors['min_len'] = 'too small'
        if self.options['contain_numbers'] and not self._has_number(check):
            self.errors['contain_numbers'] = 'should contain at least one numb'
        return self.errors

    def is_check_length(self, check):
        if len(check) < self.OPTIONS['min_len']:
            return True
        return False

    # END

    def _has_number(self, password):
        return any(char.isdigit() for char in password)


# validator = PasswordValidator()
# errors = validator.validate('qwerty1')
# print(errors)  # => {'min_len': 'too small'}

options = {'contain_numbers': False}
validator = PasswordValidator(**options)
errors = validator.validate('another-password')
print(errors)

# # валидатор должен игнорировать несуществующие опции
# validator = PasswordValidator(numberz=None)
# errors = validator.validate('qwertya3sdf')
# print(errors) # => {}
