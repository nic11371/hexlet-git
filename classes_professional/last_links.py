class Base:
    def is_instance_of(self, obj):
        classes = self.__class__.__mro__
        name_classes = []
        for c in classes:
            name_classes.append(c.__name__)
        return obj in name_classes


class Child(Base):
    pass


class ChildOfChild(Child):
    pass


obj = ChildOfChild()
print(obj.is_instance_of('Base'))
print(obj.is_instance_of('Child'))
print(obj.is_instance_of('ChildOfChild'))
print(obj.is_instance_of('SomeClass'))
