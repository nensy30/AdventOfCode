#Day 4: Scratchcards
from collections import Counter
from collections import defaultdict

cards_str = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

total_points = 0 
scratchcards = defaultdict(int)
total_scratchcards = 0 
cards = cards_str.split('\n')

i = 1
for card in cards:
    card_id, card_list = card.split(':')
    set1, set2 = card_list.split('|')
    set1_nums = set([int(n) for n in set1.split()])
    set2_nums = set([int(n) for n in set2.split()])

    common_values = set1_nums & set2_nums
   
    len_common_values = len(common_values)
    if len_common_values > 0: 
        total_points += 2**(len_common_values-1)
    scratchcards[i] += 1
    for j in range(i + 1, i + len_common_values + 1):
        scratchcards[j] += scratchcards[i]
    i+=1
for key, value in scratchcards.items():
    total_scratchcards += value
    
print(f"Total points are: {total_points}")
print(f"Total scratchcards are: {total_scratchcards}") 
