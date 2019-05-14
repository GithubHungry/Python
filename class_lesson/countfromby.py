class CountFromBy:
    def __init__(self, v: int = 0, i: int = 1) -> None:  # like a constructor
        """Initialization"""
        self.val = v
        self.incr = i

    def __repr__(self) -> str:
        """Represented"""
        return str(self.val)  # will return string-value attr val

    def increase(self) -> None:
        """This method increases the number by the specified number."""
        self.val += self.incr  # Take from object value and step


# g = CountFromBy(100, 10)
# print(g.val)
# print(g.incr)
# print(g)
# g.increase()
# print(g.val)
# print(g.incr)

# obj2 = CountFromBy(100, 10)
# print(obj2)
# print(type(obj2))
# print(id(obj2))  # information about address obj2 in memory = use as id
# print(hex(id(obj2)))

default = CountFromBy(i=10)
print(default)
print(default.val)
print(default.incr)
for i in range(10):
    default.increase()
print(default)
