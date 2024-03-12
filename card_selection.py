def card_selection(player, card_play):
    played_cards = []
    if card_play == 'sc':
        number_of_cards = 1
    else:
        while True:
            try:
                number_of_cards = int(
                    input('How many cards would you like to play? '))
                break
            except ValueError:
                print("Invalid input. Please enter an integer")

    for i in range(number_of_cards):
        pick_card = input(f'Type card number {i+1}: ')
        if (pick_card in players_cards[player-1]) and (pick_card not in played_cards):
            played_cards.append(pick_card)
        else:
            while (pick_card not in players_cards[player-1]) or (pick_card in played_cards):
                pick_card = input(f'Type card number {i+1}: ')
            played_cards.append(pick_card)

    return played_cards
