from typing import List

# list_numbers = [6, 4, 3, 5, 2, 1]

#
#
# def function_list(numbers: list) -> int:
#     temp = numbers[0]
#     for i in range(1, len(numbers)):
#         if numbers[i] > temp:
#             temp = numbers[i]
#     return temp
#
#
# print(function_list(list_numbers))
#

# # eleventh question
# def digit_to_list_convertor(numb: int) -> list:
#     # return [int(i) for i in str(numb)]
#     return [int(i) for i in str(numb)]
#
#
# print(digit_to_list_convertor(45789008765432))


# def digit_to_list_convertor(numb: int, ) -> list:
#     list_of_numb = []
#
#     for i in str(numb):
#         list_of_numb.append(int(i))
#         return list_of_numb
#
#     print(digit_to_list_convertor(45646))
#     question 9
# def list_concate(list_one: list, list_two: list) -> list:
#     return list_one + list_two


# print(list_concate(list_numbers, list_numbers))
# question 1
list_numbers = [9, 4, 3, 5, 2, 1]


def function_list(numbers: list) -> int:
    temp = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > temp:
            temp = numbers[i]
    return temp


print(function_list(list_numbers))

# question 2

# returning numbers backward
list_numbers = [10, 20, 30, 40, 50, 60]


def list_reverserse(digit: list) -> list[int]:
    jump = digit[::-1]
    return jump


print(list_reverserse(list_numbers))

# question 3
list_counting = [2, 4, 6, 8, 10]


# def list_checkers(arr: list) -> list[int]:
#     for i in range(len(arr), 1):
#         if list_counting == arr[list]:
#             print(list_counting)
def list_checker(element, ls):
    result = False
    if element in ls:
        result = True
    return result


print(list_checker(10, list_counting))


# question 4
def list_odd(vab: list) -> list:
    check = vab[::-2]
    return check


print(list_odd(list_numbers))


# question 5
def list_even(jay: list) -> list:
    select = jay[::+2]
    return select


print(list_even(list_numbers))


# question 6


def list_total(list_one: list) -> int:
    total = 0
    for i in range(0, len(list_one), 1):
        total += list_one[i]
    return total


print(list_total(list_numbers))

# question 9
list_numbers = [6, 4, 3, 5, 2, 1]


def list_concate(list_one: list, list_two: list) -> list:
    return list_one + list_two


print(list_concate(list_numbers, list_numbers))

# question 11
list_numbers = [7, 4, 3, 5, 2, 1]


def digit_to_list_convertor(numb: int) -> list:
    return [int(i) for i in str(numb)]


print(digit_to_list_convertor(45789008765432))
