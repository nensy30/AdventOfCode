#Day 8: Haunted Wasteland
#Part 1

data ="""LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

directions, _, *net= data.split('\n')

network = {}
for n in net:
    position, targets = n.split(" = ")
    network[position] = targets[1:-1].split(", ")

steps_count = 0
start_element = 'AAA'
end_element = 'ZZZ'

while start_element != 'ZZZ':
    steps_count += 1
    start_element = network[start_element][0 if directions[0] == 'L' else 1]
    directions = directions[1:] + directions[0]

print(f"Steps are required to reach ZZZ: {steps_count}")
