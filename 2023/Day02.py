#Day 2: Cube Conundrum

games_str = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

game_possible = {'red': 12, 'green': 13, 'blue': 14}

games = games_str.split('\n')
for game in games:
  game_id, game_list = game.split(':')
  ball_list= []
  for sets in game_list.split(';'):
    for balls in sets.split(','):
      nr, color = balls.split()
      ball_list.append((color, int(nr)))
  sum_balls = {}
  for color, value in ball_list:
      sum_balls[color] = sum_balls.get(color, 0) + value

  is_posible = False
  for key in game_possible:
    if key in sum_balls and sum_balls[key] <= game_possible[key]:
      is_posible = True
    else:
      is_posible = False
      break
  print(game_id, sum_balls)
  if is_posible == True : print(game_id + ' is possible.')
