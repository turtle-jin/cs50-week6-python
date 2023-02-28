from cs50 import get_string


# Prompt for input
num = get_string("Number: ")

if len(num) % 2 == 0:  # the number has even numbered total digits
    even_string_list = list(num[::2])
    odd_string_list = list(num[1::2])

else:  # num has odd number of total digits
    even_string_list = list(num[1::2])
    odd_string_list = list(num[::2])

# convert list of strings to list of integers with list comprehension
even_list = [int(i) for i in even_string_list]
odd_list = [int(i) for i in odd_string_list]

# print(f"even list is :{even_list}")
# print(f"odd list is: {odd_list}")

# calculate doubled sum in even list
even_sum = 0
for digit in even_list:
    doubled = digit * 2
    if doubled <= 9:
        even_sum += doubled
    else:
        ones_value = doubled - 10
        doubled = 1 + ones_value
        even_sum += doubled

# calculate sum in odd list
odd_sum = 0
for digit in odd_list:
    odd_sum += digit

# calculate total
total = even_sum + odd_sum

# check type of card
if total % 10 != 0:
    print("INVALID")
else:
    if len(num) == 15 and (num[:2] == "34" or num[:2] == "37"):
        print("AMEX")
    elif len(num) == 16 and (int(num[:2]) >= 51 and int(num[:2]) <= 55):
        print("MASTERCARD")
    elif (len(num) == 13 or len(num) == 16) and num[0] == "4":
        print("VISA")
    else:
        print("INVALID")