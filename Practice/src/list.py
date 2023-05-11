
def function_list(sum_list):
    count = 0
    for i in sum_list:
        count += i
    return count


list_numbers = [2, 3, 4, 5, 6, 7, 8, 9, ]
print(function_list(list_numbers))
