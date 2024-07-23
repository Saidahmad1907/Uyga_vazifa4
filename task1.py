
class String:
    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        instance.__dict__[self._name] = value

    def __set_name__(self, owner, name):
        self._name = name


class Person:
    name = String()

    def __init__(self, name):
        self.name = name

p = Person("John Doe")
print(p.name)  

p.name = "Jane Doe"
print(p.name)  

try:
    p.name = 123  
except ValueError as e:
    print(e)  
