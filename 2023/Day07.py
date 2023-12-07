example_str = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

cards_set_dict = {"A":"14", "K":"13", "Q":"12", "J":"11", "T":"10", "9":"09", "8":"08", "7":"07", "6":"06", "5":"05", "4":"04", "3":"03", "2":"02"}
cards_set_dict_joker = {"A":"14", "K":"13", "Q":"12", "T":"10", "9":"09", "8":"08", "7":"07", "6":"06", "5":"05", "4":"04", "3":"03", "2":"02", "J":"01",}


def card_characterize(s):
    cnts = Counter(s)
    vals = sorted(cnts.values())
    print(s,vals)    
    if vals[-1] == 5:
        return 10
    elif vals[-1] == 4:
        return 9
    elif vals == [2, 3]:
        return 8
    elif vals == [1, 1, 3]:
        return 7
    elif vals == [1, 2, 2]:
        return 6
    elif vals == [1, 1, 1, 2]:
        return 5
    elif vals == [1, 1, 1, 2]:
        return 4
    else:
        return 3

camels = example_str.split('\n')
camels_card = []
for c in camels:
    card_type, card_value = c.split(' ')
    sort_result = ''.join(cards_set_dict[char] if char in cards_set_dict else char for char in card_type)
    sort_result_joker = ''.join(cards_set_dict_joker[char] if char in cards_set_dict_joker else char for char in card_type)
    rank_result  = card_characterize(card_type)
    camels_card.append((rank_result, sort_result, sort_result_joker, card_type, int(card_value)))

sorted_camels_card = sorted(camels_card, key=lambda x: (x[0], x[1]))
sorted_camels_joker = sorted(camels_card, key=lambda x: (x[0], x[2]))
print(sorted_camels_card)
print(sorted_camels_joker)
total_win = 0
i = 1
for card in sorted_camels_card:
    total_win += (card[4] * i)
    i+=1

total_win_joker = 0
j = 1
for card in sorted_camels_joker:
    total_win_joker += (card[4] * j)
    j+=1

print (total_win)

print (total_win_joker)
