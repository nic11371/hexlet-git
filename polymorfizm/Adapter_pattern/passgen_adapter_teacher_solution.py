from polymorfizm.Adapter_pattern.passgen import generate_password


# BEGIN
class PasswordGeneratorAdapter:
    def generate_password(self, length, options):
        default_options = {
            'uppercase': False,
            'digits': False,
            'symbols': False,
        }
        prepared_options = {key: True for key in options}
        final_options = {**default_options, **prepared_options}
        return generate_password(length, **final_options)
# END
