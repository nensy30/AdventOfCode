example_str ="""Time:      7  15   30
Distance:  9  40  200"""

t_val, d_val = example_str.split('\n')
times = list(map(int, t_val.split()[1:]))
distances = list(map(int, d_val.split()[1:]))
 
def number_of_ways(time, distance):
    nr_ways = 0
    for i in range(time+1):
        dist = i*(time-i)
        if dist > distance: nr_ways +=1 
    return nr_ways

total_nr_ways = 1
for t, d in zip(times, distances):
    nr_ways = number_of_ways(t, d)
    total_nr_ways *= nr_ways
print(f"Part one total nr ways: {total_nr_ways}")

    
time_2 = int(t_val.replace(" ","").split(":")[1])
distance_2 = int(d_val.replace(" ","").split(":")[1])

total_nr_ways_2 = number_of_ways(time_2, distance_2)
print(f"Part two total nr ways: {total_nr_ways_2}")
