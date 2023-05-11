first_number = int(input("Enter first integer"))
second_number = int(input("Enter second integer"))
third_number = int(input("Enter third integer"))
forth_number = int(input("Enter forth integer"))
fifth_number = int(input("Enter fifth integer"))

smallestNumber = 0
largestNumber = 0

if first_number < smallestNumber:
    smallestNumber = first_number
if first_number > largestNumber:
    largestNumber = first_number
if second_number > smallestNumber:
    smallestNumber = second_number
if second_number < largestNumber:
    largestNumber = second_number
if third_number < smallestNumber:
    smallestNumber = third_number
if third_number > largestNumber:
    largestNumber = third_number
if forth_number < smallestNumber:
    smallestNumber = forth_number
if forth_number > largestNumber:
    largestNumber = forth_number
if fifth_number < smallestNumber:
    smallestNumber = fifth_number
if fifth_number > largestNumber:
    largestNumber = fifth_number

print(smallestNumber, ": is a smallest number")
print(largestNumber, " :is a largest number")

