import random
yaniv = False
card_count = 0
card_values = {"1": 1, "2": 2, "3": 3, "4": 4,
               "5": 5, "6": 6, "7": 7, "8": 8,
               "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "0": 0
               }


def shuffle_fresh_pack():
    jokers = ["J0", "J0"]
    suits = ["S", "C", "D", "H"]
    values = ["2", "3", "4", "5", "6", "7",
              "8", "9", "10", "J", "Q", "K"]
    unshuffled_cards = [
        suit+value for suit in suits for value in values] + jokers
    shuffled_cards = list(unshuffled_cards)
    random.shuffle(shuffled_cards)
    return shuffled_cards


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


players = 3
players_cards, cards, faced_up_pile = deal_fresh_pack(players)


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


def check_single_card(played_cards):
    if len(played_cards) != 1:
        print('Invalid Play, Try Again')
        played_cards.clear()

    return played_cards


def check_set(played_cards):
    set_check = [card[1:] for card in played_cards if card[0] != "J"]
    if (len(set(set_check)) != 1) or (len(played_cards)) == 1:
        print('Invalid Play, Try Again')
        played_cards.clear()

    return played_cards


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


def check_joker_seq(played_cards):
    suit_check = [card[0] for card in played_cards]
    if (len(set(suit_check)) == 2) and (len(played_cards) >= 3):
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


def call_yaniv(player):
    global yaniv
    player_scores = [[] for i in range(len(players_cards))]

    for players in range(len(players_cards)):
        for cards in players_cards[players]:
            player_scores[players].append(card_values.get(cards[1:]))

    player_scores = [sum(cards) for cards in player_scores]

    winner_index = [idx for idx, score in enumerate(
        player_scores) if score == min(player_scores)]

    if player_scores[player-1] > 5:
        print('Your card hand score is above 5')
        print('We will return to the game.')

    elif (player_scores[player-1] <= 5) and ([player_scores.index(player_scores[player-1])]) == winner_index:
        yaniv = True
        print(f"""Player {player} called yaniv and won with a score of {
              player_scores[player-1]}""")
        print('The final scores are:')
        for i in range(players+1):
            print(f'Player {i+1}: {player_scores[i]}')

    elif player_scores.index(player_scores[player-1]) != winner_index:
        yaniv = True
        print(f"""Player {player} called yaniv with a score of {
              player_scores[player-1]}.""")
        for i in winner_index:
            if i == player:
                continue
            print(f'But player {i+1} scored {player_scores[i]}')

        print(f'Player {player} loses.')
        print('The final scores are:')
        for i in range(players+1):
            print(f'Player {i+1}: {player_scores[i]}')

    return yaniv


def player_greeting(player):
    print(f'Hi player {player}')
    print(f'Your hand is: {players_cards[player-1]}')
    print(f'The previous player played {card_count} card(s)')
    if (card_count == 1) or (card_count == 0):
        print(f'Top card of faced up pile is: {faced_up_pile[0]}')
    else:
        print(f'The top {card_count} cards of the faced up pile are: {faced_up_pile[:card_count]}')
    return

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


def yaniv_game():
    global yaniv
    while yaniv == False:
        for player in range(1, players+1):
            if yaniv == True:
                break
            players_cards, cards, faced_up_pile, yaniv = player_turn(player)

    return players_cards, cards, faced_up_pile, yaniv


players_cards, cards, faced_up_pile, yaniv = yaniv_game()

print(players_cards)

print(cards)

print(faced_up_pile)
