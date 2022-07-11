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


def play_combat(deck1, deck2):
    while len(deck1) != 0 and len(deck2) != 0:
        card1, card2 = deck1[0], deck2[0]
        if card1 > card2:
            deck1 = deck1[1:] + [card1, card2]
            deck2 = deck2[1:]
        else:
            deck1 = deck1[1:]
            deck2 = deck2[1:] + [card2, card1]
    return deck1 if len(deck1) > 0 else deck2


def score_calculator(deck):
    deck.reverse()
    score = 0
    multiplier = 1
    while multiplier <= len(deck):
        score += multiplier * deck[multiplier-1]
        multiplier += 1
    return score


player1, player2 = file_reader(file)
winner_deck = play_combat(player1, player2)
winner_score = score_calculator(winner_deck)
print(f'FINAL ANSWER: {winner_score}')


