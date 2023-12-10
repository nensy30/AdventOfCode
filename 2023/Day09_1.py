# Day 9 Mirage Maintenance
#       Part 1

data ="""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

rows = data.split('\n')

def extrapolate(arr):
    if all(x == 0 for x in arr):
        return 0
    deltas = [y - x for x,y in zip(arr, arr[1:])]
    diff = extrapolate(deltas)
    return arr[-1] + diff

total = 0
for row in rows:
    nums = list(map(int, row.split()))
    total += extrapolate(nums)

print(f"Part1 - Sum of extrapolated values: {total}")
