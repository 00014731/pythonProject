# Task5
# num = int(input("Enter the number: "))
# print(num)
# print(oct(num))
# print(hex(num))

# Task6
# num = int(input("Enter the number: "))
# if num % 2 == 1:
#     print("odd")
# else:
#     print("even")

# Task7
# def converter(num):
#     print(num)
#     print(oct(num))
#     print(hex(num))
#
#
# # num = int(input("Enter the number: "))
# converter(10)
# converter(111)


# def even_odd(num):
#     num_type = None
#
#     if num % 2 == 1:
#         num_type = "odd"
#     else:
#         num_type = "even"
#     return num_type
#
#
# num = int(input("Enter the number: "))
# print(even_odd(num))

def even_odd(number):
    if number % 2 == 1:
        print(number, "is odd")
    else:
        print(number, "is even")


num = int(input("Enter the number: "))
print(even_odd(num))
