class Animal:

    def __init__(self, name, age, size, color):
        self.name = name
        self.age = age
        self.size = size
        self.color = color

    def sound(self, audio="sound"):
        return f"{self.name}Animals can  {audio}"

    def __repr__(self):
        return f"{self.name} can  "


animals = Animal("goat" "cat", 4, "small", "white")
print(animals.sound())
