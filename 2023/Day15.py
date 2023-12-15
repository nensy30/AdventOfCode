# Day 15: Lens Library
# Part 1
data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""
steps = data.split(',')

def Hash_Algoritam (string):
    chars = list(string)
    t = 0
    for char in chars:
        t = (t + ord(char))*17%256
    return int(t)

total = 0
for s in steps:
    total += Hash_Algoritam(s)
print(f"Part one: {total}")

# Part 2
boxes = [[] for _ in range(256)]
focal_lenghts = {}
for s in steps:
    if "-" in s:
        label = s[:-1]
        index = Hash_Algoritam(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        label, length = s.split("=")
        length = int(length)
        index = Hash_Algoritam(label)
        
        if label not in boxes[index]:
            boxes[index].append(label)
        focal_lenghts[label] = length
    
total2 = 0
for box_num, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total2 += box_num * lens_slot * focal_lenghts[label]

print(f"Part two: {total2}")
