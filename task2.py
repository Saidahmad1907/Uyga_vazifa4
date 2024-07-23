
class Integer:
    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        instance.__dict__[self._name] = value

    def __set_name__(self, owner, name):
        self._name = name


class Example:
    number = Integer()

    def __init__(self, number):
        self.number = number

e = Example(42)
print(e.number)  

e.number = 100
print(e.number)  

try:
    e.number = "not an integer" 
except ValueError as e:
    print(e)  
