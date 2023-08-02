class MyClass:

    def __init__(self, name, age):
        self.name = name

    # name = "Lily"
    def sum(self, a, b):
        print(a + b)


# x = MyClass()
x = MyClass("Lily", 20)
# del x

print(x.name)
x.sum(4, 5)