#Day 11: Cosmic Expansion
data_str = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

data = data_str.split('\n')


rows_with_no_galaxy = [r for r, row in enumerate(data) if all(char == "." for char in row)]
col_with_no_galaxy = [c for c, col in enumerate(zip(*data)) if all(char == "." for char in col)]

points = [(r, c) for r, row in enumerate(data) for c, char in enumerate(row) if char == "#"]

total = 0
scale = 2

# Calculate total based on rows and columns without galaxy
total = sum(2 if r in rows_with_no_galaxy or c in col_with_no_galaxy else 1 for r, c in points)

print(total)
