from math import floor
def single_digit_converter(digit):
    if digit == 10:
        digit = "A"
    if digit == 11:
        digit = "B"
    if digit == 12:
        digit = "C" 
    if digit == 13:
        digit = "D" 
    if digit == 14:
        digit = "E"
    if digit == 15:
        digit = "F"
    return digit
def recursive_digit_finder(current_eval, list_of_digits):
    rem = current_eval%16
    next_eval = floor(current_eval/16)
    list_of_digits.append(rem)
    if next_eval > 16:
        recursive_digit_finder(next_eval, list_of_digits)
    else:
        list_of_digits.append(next_eval)
    return list_of_digits

numbers = input("Please enter numbers with a space between each number: ")
numbers = numbers.split(" ")
dec_values = []
for num in numbers:
    dec_values.append(int(num))
all_hex_values = ""
for dec_value in dec_values:
    list_of_digits = []
    recursive_digit_finder(dec_value, list_of_digits)
    hex_value = ""
    for digit in reversed(list_of_digits):
        hex_value = hex_value + str(single_digit_converter(digit))
    all_hex_values = all_hex_values + hex_value
print(all_hex_values)