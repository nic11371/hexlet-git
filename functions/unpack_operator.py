def format_person_info(*basic, **additional):
    # name, age = basic
    base_name = ""
    base_age = ""
    add_str = []
    for b in basic:
        if isinstance(b, str):
            base_name = f"Name: {b},"
        if isinstance(b, int):
            base_age = f"Age: {b}"
    for k, v in sorted(additional.items()):
        add_str.append(f"{k.capitalize()}: {v}")
    if add_str == []:
        return f"{base_name if base_name else ""} {base_age if base_age else ""}"
    return f"{base_name if base_name else ""} {base_age if base_age else ""}, {", ".join(add_str)}"