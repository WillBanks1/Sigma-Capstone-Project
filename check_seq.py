def check_seq(played_cards):
    played_cards = list(map(lambda card: card.replace(
        'J', '11').replace('Q', '12').replace('K', '13'), played_cards))
    suit_check = [card[0] for card in played_cards]
    number_check = sorted([int(card[1:]) for card in played_cards])

    if ((len(set(suit_check)) != 1) and
            (number_check != list(range(number_check[0], number_check[-1] + 1, 1)))) or len(played_cards) < 3:
        print('Invalid Play, Try Again')
        played_cards.clear()

    played_cards = sorted(
        played_cards, key=lambda card: int(card[1:]), reverse=True)
    played_cards = list(map(lambda card: card.replace(
        '11', 'J').replace('12', 'Q').replace('13', 'K'), played_cards))

    return played_cards
