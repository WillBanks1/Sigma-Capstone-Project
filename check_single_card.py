def check_single_card(played_cards):
    if len(played_cards) != 1:
        print('Invalid Play, Try Again')
        played_cards.clear()

    return played_cards
