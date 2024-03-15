def player_turn(player):
    global players_cards
    global cards
    global faced_up_pile
    global yaniv
    global card_count
    if not cards:
        cards = faced_up_pile.reverse()
        faced_up_pile.clear()
        faced_up_card = cards[0]
        while card_values.get(faced_up_card[1:]) < 5:
            cards.remove(cards[0])
            cards.append(faced_up_card)
            faced_up_card = cards[0]

        cards.remove(cards[0])
        faced_up_pile.append(faced_up_card)
    
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
            if "J0" in played_cards:
                played_cards = check_joker_seq(played_cards)
            else:
                played_cards = check_seq(played_cards)

    players_cards, cards, faced_up_pile = pick_card_pile(player)

    for card in played_cards:
        players_cards[player-1].remove(card)
        faced_up_pile.insert(0, card)
    
    card_count = len(played_cards)

    return players_cards, cards, faced_up_pile, yaniv
