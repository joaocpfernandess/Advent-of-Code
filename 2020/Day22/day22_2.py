file = open('input.txt', 'r')


def file_reader(file):
    p1, p2 = [], []
    l = file.readline()
    l = file.readline()
    while l != '\n':
        p1.append(int(l[:-1]))
        l = file.readline()
    l = file.readline()
    l = file.readline()
    while l:
        p2.append(int(l[:-1]))
        l = file.readline()
    return p1, p2


def recursive_combat(deck1, deck2, past_configs, lvl):
    while len(deck1) != 0 and len(deck2) != 0:
        if [deck1, deck2] in past_configs:
            return 1, deck1
        else:
            past_configs.append([deck1, deck2])
        card1, card2 = deck1[0], deck2[0]
        if len(deck1[1:]) >= card1 and len(deck2[1:]) >= card2:
            winner, win_deck = recursive_combat(deck1[1:card1+1], deck2[1:card2+1], [], lvl+1)
            if winner == 1:
                deck1 = deck1[1:] + [card1, card2]
                deck2 = deck2[1:]
            else:
                deck1 = deck1[1:]
                deck2 = deck2[1:] + [card2, card1]
        elif card1 > card2:
            deck1 = deck1[1:] + [card1, card2]
            deck2 = deck2[1:]
        else:
            deck1 = deck1[1:]
            deck2 = deck2[1:] + [card2, card1]
    return (1, deck1) if len(deck1) > 0 else (2, deck2)


def score_calculator(deck):
    deck.reverse()
    score = 0
    multiplier = 1
    while multiplier <= len(deck):
        score += multiplier * deck[multiplier-1]
        multiplier += 1
    return score


player1, player2 = file_reader(file)
my1, my2 = [9, 2, 6, 3, 1], [5, 8, 4, 7, 10]
winner, winning_deck = recursive_combat(player1, player2, [], 0)
winning_score = score_calculator(winning_deck)


print(f'FINAL ANSWER: {winning_score}')
