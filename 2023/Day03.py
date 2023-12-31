from ast import And
import re
example_engine = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

special_characters = "!@#$%^&*()-_+=<>?/[]{}|"

def is_part_number(begin_index, end_index, part_string):
  if begin_index > 0 : begin_index = begin_index - 1
  if end_index < len(part_string) : end_index = end_index + 1

  substring = part_string[begin_index:end_index]
  for char in substring:
    if char in special_characters:
      return True
  return False

engine = example_engine.split('\n')
engine_len = len(engine)
part_number = []
for l in range(engine_len):
  prev_line = ""
  next_line = ""
  curr_line = engine[l]
  if l > 0 : prev_line = engine[l - 1]
  if l < len(engine) - 1 : next_line = engine[l + 1]

  char_curr_line = [char for char in curr_line]
  #char_prev_line = [char for char in prev_line] if prev_line != "" else []
  #char_next_line = [char for char in curr_line] if curr_line != "" else []

  number = ""
  char_index = 0;
  for char in char_curr_line:
    if char.isdigit() and char_index != len(char_curr_line)-1 :
      number += char 
    elif char_index == len(char_curr_line)-1 and char.isdigit():
      number += char 
      #check if it is part number
      begin_index = char_index - len(number)
      #in current line
      if number != "":
        if is_part_number(begin_index, char_index, curr_line):
          part_number.append(int(number))
          number = ""
      #in previus line
      if prev_line != "" and number != "":
        if is_part_number(begin_index, char_index, prev_line):
          part_number.append(int(number))
          number = ""            
      #in next line
      if next_line != "" and number != "":
        if is_part_number(begin_index, char_index, next_line):
          part_number.append(int(number))            
          number = ""   
    else:
      #check if it is part number
      begin_index = char_index - len(number)
      #in current line
      if number != "":
        if is_part_number(begin_index, char_index, curr_line):
          part_number.append(int(number))
          number = ""
      #in previus line
      if prev_line != "" and number != "":
        if is_part_number(begin_index, char_index, prev_line):
          part_number.append(int(number))
          number = ""            
      #in next line
      if next_line != "" and number != "":
        if is_part_number(begin_index, char_index, next_line):
          part_number.append(int(number))            
          number = ""

    char_index += 1;

print("Part numbers are", part_number)

total_sum = sum(part_number)

print(f"The sum of all of the part numbers in the engine schematic is: {total_sum}")
