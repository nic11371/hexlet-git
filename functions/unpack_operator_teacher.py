def format_person_info(name, age, **kwargs):
    base_info = f"Name: {name}, Age: {age}"

    if kwargs:
        additional_info = []
        for key, value in sorted(kwargs.items()):
            additional_info.append(f"{key.capitalize()}: {value}")
        return f"{base_info}, {", ".join(additional_info)}"
    else:
        return base_info
