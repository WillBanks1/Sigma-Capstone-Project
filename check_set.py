def check_set(played_cards):
    set_check = [card[1:] for card in played_cards if card[0] != "J"]
    if (len(set(set_check)) != 1) or (len(played_cards)) == 1:
        print('Invalid Play, Try Again')
        played_cards.clear()

    return played_cards
