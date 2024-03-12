def first_dealer(players):
    cards = shuffle_fresh_pack()
    dealer = []
    for i in range(0, players):
        x = random.choice(cards)
        cards.remove(x)
        dealer.append(card_values.get(x[1:]))
    dealer = [(f'Player {idx}', score) for idx, score in enumerate(dealer, 1)]
    return dealer
