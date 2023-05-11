import pip as pip

pip: pip
print("numbers\t", "cubes\t\t", "square")
number = 0
while number <= 9:
    number = number + 1
    cubes = number * number * number
    squareOfNumber = number * number
    print(number, "\t\t", squareOfNumber, "\t\t", cubes)
 