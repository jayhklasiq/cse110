import os
os.system('cls')

import math


numbers = []
digits_entered = None
# total_add_up = 0
digit_count = -1

while digits_entered != 0:
    digits_entered = int(input('Enter a list of numbers, type 0 when finished. '))
    if digits_entered != 0:
        numbers.append(digits_entered)
    digit_count += 1

add_up_numbers = sum(numbers)
average_of_numbers = add_up_numbers / len(numbers)
#req1
print(add_up_numbers)

#req2
print (f'Your average is {average_of_numbers:.2f}')

#req3
large_number = -1
for number in numbers:
    if number > large_number:
        large_number = number
print (f'The largest number is {large_number}')

#req4
lowest_positive_num = 555555555
for number in numbers:
    if number > 0 and number < lowest_positive_num:
        lowest_positive_num = number 
print (f'The lowest positive number is {lowest_positive_num}')

numbers.sort()

print(numbers)
