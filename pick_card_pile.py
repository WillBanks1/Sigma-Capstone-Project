def pick_card_pile(player):
    which_pile = input("""Which pile are you going to take a card from?
                           faced up (type 'u') or faced down (type 'd') """)
    while (which_pile != 'u') and (which_pile != 'd'):
        print("You must enter either 'u' or 'd'")
        which_pile = input("""Which pile are you going to take a card from?
                           faced up (type 'u') or faced down (type 'd') """)
    if which_pile == 'd':
        players_cards[player-1].append(cards[0])
        cards.remove(cards[0])
    
    elif which_pile == 'u':
        if card_count > 1:
            card_choice = input(f'You can take either {faced_up_pile[0]} or {faced_up_pile[card_count-1]} ')
            while (card_choice != faced_up_pile[0]) and (card_choice != faced_up_pile[card_count-1]):
                print("Invalid card choice.")
                card_choice = input(f'You can take either {faced_up_pile[0]} or {faced_up_pile[card_count-1]} ')
        else:
            card_choice = faced_up_pile[0]
        
        players_cards[player-1].append(card_choice)
        faced_up_pile.remove(card_choice)

    return players_cards, cards, faced_up_pile