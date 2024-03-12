def deal_fresh_pack(players):
    card_count = 0
    cards = shuffle_fresh_pack()
    players_cards = [[] for i in range(players)]
    faced_up_pile = []
    while card_count < 5:
        card_count += 1
        for players in players_cards:
            dealt_card = cards[0]
            cards.remove(dealt_card)
            players.append(dealt_card)

    faced_up_card = cards[0]
    while card_values.get(faced_up_card[1:]) < 5:
        cards.remove(cards[0])
        cards.append(faced_up_card)
        faced_up_card = cards[0]

    cards.remove(cards[0])
    faced_up_pile.append(faced_up_card)
    return players_cards, cards, faced_up_pile
