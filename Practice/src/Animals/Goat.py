from Animal import Animal


class Goat(Animal):
    def __init__(self, horn):
        super().self.horn = horn

    def sound(self, audio):
        return super().sound(audio)

    def __repr__(self, sound="bleat") -> str:
        return f" {super(Goat, self).sound()}"


animals = Goat("goat", 4, "small", "white")
print(animals.sound("bleed"))
print(animals)
