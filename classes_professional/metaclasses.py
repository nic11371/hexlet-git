class MyMeta(type):
    def __init__(cls, name, bases, attrs):
        print(f"Создание класса {name}")
        super().__init__(name, bases, attrs)


class MyClass(metaclass=MyMeta):
    pass  # Создание класса MyClass
