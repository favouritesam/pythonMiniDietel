first_number = int(input("Enter first Integer"))
second_number = int(input("Enter second Integer"))
third_number = int(input("Enter third Integer"))
forth_number = int(input("Enter forth Integer"))
fifth_number = int(input("Enter fifth Integer"))

positive_Number = 0
negative_Number = 0
numberOfZeros = 0

if first_number > 0:
    positive_Number += 1

if first_number < 0:
    negative_Number += 1

if first_number == 0:
    numberOfZeros += 1

if second_number > 0:
    positive_Number += 1

if second_number < 0:
    negative_Number += 1

if second_number == 0:
    numberOfZeros += 1

if third_number > 0:
    positive_Number += 1

if third_number < 0:
    negative_Number += 1

if third_number == 0:
    numberOfZeros += 1

if forth_number > 0:
    positive_Number += 1

if forth_number < 0:
    negative_Number += 1

if forth_number == 0:
    numberOfZeros += 1

if fifth_number > 0:
    positive_Number += 1

if fifth_number < 0:
    negative_Number += 1

if fifth_number == 0:
    numberOfZeros += 1

print("positive number is", '=', positive_Number)
print("negative number is", '=', negative_Number)
print("number of zeros is", '=', numberOfZeros)
