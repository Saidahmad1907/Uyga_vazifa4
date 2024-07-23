
class Float:
    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._name)

    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError("Value must be a float")
        instance.__dict__[self._name] = value

    def __set_name__(self, owner, name):
        self._name = name


class Example:
    value = Float()

    def __init__(self, value):
        self.value = value

e = Example(3.14)
print(e.value)  

e.value = 2.71
print(e.value)  

try:
    e.value = "not a float"  
except ValueError as e:
    print(e)  
