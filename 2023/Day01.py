# Day 1: Trebuchet?!
#The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

import re
example_values = ["1abc2",
          "pqr3stu8vwx",
          "a1b2c3d4e5f",
          "treb7uchetG"]
sum_digit_values = 0
for value in example_values:
  nums = re.findall(r'\d+', value)
  digit = int(nums[0] + nums[len(nums)-1]) if nums else 0
  sum_digit_values += digit
print ("Sum of all of the calibration values is " + str(sum_digit_values))
