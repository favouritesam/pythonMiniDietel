#     if user_input % 4 == 0:
#         print("user input {}")
# int_user_input = [20, 30.40, 50, 60, 70, 80]
#
# i = eval(input("Enter 1 to play"))
# while i != -1:
#     user_input = int(input("Enter any number of choice:"))
#     if user_input % 2 == 0:
#         print("This number is an even number")
#     else:
#         print("it is and odd number")
#     if user_input % 4 == 0:
#         print("it is a multiple of 4")
#     i = eval(input("do you still want to continue? \n enter -1 to quit or 1 to continue"))
#

#   question two
user_Input = int(input("Enter any number of ur choice:"))
number_Checker = int(input("Enter one number to check call user-number"))
if number_Checker % user_Input == 0:
    print("successful")
else:
    print("fail")




