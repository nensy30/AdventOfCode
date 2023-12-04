# Day 1: Trebuchet?!
#The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

import re
example_values_str = """1abc2one
pqr3stu8vwx
a1b2c3d4e55f
treb7uchettwot"""

def sum_values (values_list):
    sum_digit_values = 0
    for value in values_list:
        nums = re.findall(r'\d+', value)
        first_num = nums[0]
        last_num = nums[len(nums)-1]
        digit = int(first_num[0] + last_num[-1]) if nums else 0
        sum_digit_values += digit
    return sum_digit_values

example_values_list = example_values_str.split('\n')
print (f"Sum of all of the calibration values is {sum_values(example_values_list)}")

#sum of all of the calibration values
number_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

example_repl_values_str = example_values_str
for key, value in number_dict.items():
    example_repl_values_str = example_repl_values_str.replace(value, str(key))

example_repl_values_list = example_repl_values_str.split('\n')

print (f"Sum of all of the calibration values is {sum_values(example_repl_values_list)}")
