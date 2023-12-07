#Day 2: Cube Conundrum
from functools import reduce
from operator import mul

games_str = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

game_possible = {'red': 12, 'green': 13, 'blue': 14}

games = games_str.split('\n')
games_IDs_total = 0
games_score_total = 0
for game in games:
    is_true = True
    game_id_val, game_list = game.split(':')
    game_id = int(game_id_val.split(" ")[1])
    ball_list = []
    for sets in game_list.split(';'):
        pairs = sets.split(', ')
        set_color_dict = {}
        for pair in pairs:
            count, color = pair.lstrip().split(' ')
            set_color_dict[color] = int(count)
        is_greater = all(set_color_dict.get(key, 0) <= game_possible.get(key, 0) for key in set(set_color_dict) | set(game_possible))
        if is_greater == False: is_true = False
        ball_list.append(set_color_dict)

    #Part 1
    if is_true: games_IDs_total += game_id
    
    #Part 2
    max_values_dict = {}
    for b in ball_list:
        for key, value in b.items():
            max_values_dict[key] = max(value, max_values_dict.get(key, float('-inf')))
    result = 1
    for value in max_values_dict.values():
        result *= value
    games_score_total += result
    
print(f"Part1 - Sum of the IDs: {games_IDs_total}")  
print(f"Part2 - Score is: {games_score_total}")  
