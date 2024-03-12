def player_turn(player):
    global yaniv
    player_greeting(player)
    played_cards = []
    while played_cards == []:
        card_play = input("""What card play would you like to make?
                          Single Card (type 'sc'), Set (type 'set') or Sequence (type 'seq') 
                          or call yaniv? (type 'yaniv') """)
        if card_play == 'yaniv':
            yaniv = call_yaniv(player)
            if yaniv == True:
                return players_cards, cards, faced_up_pile, yaniv
            else:
                card_play = input("""What card play would you like to make?
                          Single Card (type 'sc'), Set (type 'set') or Sequence (type 'seq') 
                          or call yaniv? (type 'yaniv') """)

        played_cards = card_selection(player, card_play)

        if card_play == 'sc':
            played_cards = check_single_card(played_cards)
        elif card_play == 'set':
            played_cards = check_set(played_cards)
        elif card_play == 'seq':
            played_cards = check_seq(played_cards)

    which_pile = input("""Which pile are you going to take a card from?
                           faced up (type 'u') or faced down (type 'd') """)

    while (which_pile != 'u') and (which_pile != 'd'):
        print("You must enter either 'u' or 'd'")
        which_pile = input("""Which pile are you going to take a card from?
                           faced up (type 'u') or faced down (type 'd') """)

    if which_pile == 'u':
        players_cards[player-1].append(faced_up_pile[0])
        faced_up_pile.remove(faced_up_pile[0])

    elif which_pile == 'd':
        players_cards[player-1].append(cards[0])
        cards.remove(cards[0])

    for card in played_cards:
        players_cards[player-1].remove(card)
        faced_up_pile.insert(0, card)

    return players_cards, cards, faced_up_pile, yaniv
