class Dog:
    # class attribute must be Black,Black is the class attribute.
    color = "Black"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    # def __str__(self):
    # def about(self):
    # return f"I am {self.name} of breed {self.breed}"

    # ur representation can be
    def __repr__(self):
        return f"Dog({self.name},{self.breed},{self.age}"

    def make_sound(self):
        return f"{self.name} says woof woof"


tommy = Dog("tommy", "caucasian", 5)
flip = Dog("flip", "gettttrman  shepherd", 3)
# print(tommy == flip)
# print(flip)
# print(type(tommy) == type(flip))
# print(tommy.color)
# print(tommy)
print(repr(tommy))

