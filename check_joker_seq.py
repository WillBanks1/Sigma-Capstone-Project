def check_joker_seq(played_cards):
    suit_check = [card[0] for card in played_cards]
    if len(set(suit_check)) == 2:
        seq1 = list(map(lambda card: card[0] + card[1:].replace(
            'J', '11').replace('Q', '12').replace('K', '13'), played_cards))
        seq1 = sorted([card for card in seq1 if card[0] != "J"],
                      key=lambda card: int(card[1:]))
        seq2 = list(range(int(seq1[0][1:]), int(seq1[-1][1:])+1, 1))
        seq2 = [seq1[0][0] + str(i) for i in seq2]

        for i in range(len(seq2)):
            if seq2[i] not in seq1:
                seq1.insert(i, "J0")

        if seq1.count("J0") == played_cards.count("J0"):
            played_cards = seq1
        elif seq1.count("J0") < played_cards.count("J0"):
            joker_count = played_cards.count("J0") - seq1.count("J0")
            seq1 += ["J0"] * joker_count
            played_cards = seq1
        else:
            played_cards.clear()

        played_cards.reverse()
        played_cards = list(map(lambda card: card[0] + card[1:].replace(
            '11', 'J').replace('12', 'Q').replace('13', 'K'), played_cards))
    else:
        played_cards.clear()

    return played_cards


print(check_joker_seq(played_cards))
