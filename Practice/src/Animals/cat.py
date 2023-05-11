from Animals.Animal import Animal


class cat(Animal):
    def __init__(self, tail, name, age, size, color):
        super().__init__(name, age, size, color)
        super().self.tail = tail

    def sound(self, audio):
        return super().sound(audio)

    def __repr__(self, sound="meow") -> str:
        return f" {super(cat, self).sound()}"


animals = cat("dog", 4, "small", "black")
print(animals.sound("meow"))
print(animals)
