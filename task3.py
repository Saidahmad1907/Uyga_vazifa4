class MyList:
    def __init__(self):
        self._name = None

    def __get__(self, instance, owner):
        return instance.__dict__.get(self._name)

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError("Value must be a list")
        instance.__dict__[self._name] = value

    def __set_name__(self, owner, name):
        self._name = name


class Example:
    items = MyList()

    def __init__(self, items):
        self.items = items

e = Example([1, 2, 3])
print(e.items)  

e.items = [4, 5, 6]
print(e.items)  

try:
    e.items = "not a list" 
except ValueError as e:
    print(e)  
