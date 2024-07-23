
class Boolean:
    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._name)

    def __set__(self, instance, value):
        if not isinstance(value, bool):
            raise ValueError("Value must be a boolean")
        instance.__dict__[self._name] = value

    def __set_name__(self, owner, name):
        self._name = name


class Example:
    flag = Boolean()

    def __init__(self, flag):
        self.flag = flag

e = Example(True)
print(e.flag)  

e.flag = False
print(e.flag)  

try:
    e.flag = "not a boolean"  
except ValueError as e:
    print(e)  

