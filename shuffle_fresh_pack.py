import random
yaniv = False
card_values = {"1": 1,"2": 2,"3": 3,"4": 4,
               "5": 5,"6": 6,"7": 7,"8": 8,
               "9": 9,"10": 10,"J": 10,"Q": 10,"K": 10,"0": 0
               }

def shuffle_fresh_pack():
    jokers = ["J0","J0"]
    suits = ["S","C","D","H"]
    values = ["2","3","4","5","6","7",
              "8","9","10","J","Q","K"]
    unshuffled_cards = [suit+value for suit in suits for value in values]
    shuffled_cards = list(unshuffled_cards)
    random.shuffle(shuffled_cards)
    return shuffled_cards
    
def first_dealer(players):
    cards = shuffle_fresh_pack()
    dealer = []
    for i in range(0,players):
        x = random.choice(cards)
        cards.remove(x)
        dealer.append(card_values.get(x[1:]))
    dealer = [(f'Player {idx}',score) for idx,score in enumerate(dealer,1)]
    return dealer

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
players_cards,cards,faced_up_pile = deal_fresh_pack(players)

def card_selection(player,card_play):
    played_cards = []
    if card_play == 'sc':
        number_of_cards = 1
    else:
        while True:
            try:
                number_of_cards = int(input('How many cards would you like to play? '))
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
    set_check = [card[1:] for card in played_cards]
    if (len(set(set_check)) != 1) or (len(played_cards)) == 1:
        print('Invalid Play, Try Again')
        played_cards.clear()

    return played_cards

def check_seq(played_cards):
    played_cards = list(map(lambda card: card.replace('J','11').replace('Q','12').replace('K','13'),played_cards))
    suit_check = [card[0] for card in played_cards]
    number_check = sorted([int(card[1:]) for card in played_cards])

    if ((len(set(suit_check)) != 1) and 
           (number_check != list(range(number_check[0],number_check[-1] + 1,1)))):
        print('Invalid Play, Try Again')
        played_cards.clear()
        
    played_cards = sorted(played_cards, reverse = True)
    played_cards = list(map(lambda card: card.replace('11','J').replace('12','Q').replace('13','K'),played_cards))
    
    return played_cards

def call_yaniv(player):
    global yaniv
    player_scores = [[] for i in range(len(players_cards))] 

    for players in range(len(players_cards)):
        for cards in players_cards[players]:
            player_scores[players].append(card_values.get(cards[1:]))
    
    player_scores = [sum(cards) for cards in player_scores]

    winner_index = [idx for idx, score in enumerate(player_scores) if score == min(player_scores)]

    if player_scores[player-1] > 5:
        print('Your card hand score is above 5')
        print('We will return to the game.')

    elif (player_scores[player-1] <= 5) and ([player_scores.index(player_scores[player-1])]) == winner_index:
        yaniv = True
        print(f'Player {player} called yaniv and won with a score of {player_scores[player-1]}')
        print('The final scores are:')
        for i in range(players+1):
            print(f'Player {i+1}: {player_scores[i]}')

    elif player_scores.index(player_scores[player-1]) != winner_index:
        yaniv = True
        print(f'Player {player} called yaniv with a score of {player_scores[player-1]}.')
        for i in winner_index:
            if i == player:
                continue
            print(f'But player {i+1} scored {player_scores[i]}')

        print(f'Player {player + 1} loses.')
        print('The final scores are:')
        for i in range(players+1):
            print(f'Player {i+1}: {player_scores[i]}')

    return yaniv

def player_greeting(player):
    print(f'Hi player {player}')
    print(f'Your hand is: {players_cards[player-1]}')
    print(f'Top card of faced up pile is: {faced_up_pile[0]}')
    return 

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
                return players_cards,cards,faced_up_pile, yaniv
            else:
                card_play = input("""What card play would you like to make?
                          Single Card (type 'sc'), Set (type 'set') or Sequence (type 'seq') 
                          or call yaniv? (type 'yaniv') """)
    
        played_cards = card_selection(player,card_play)

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
  
    return players_cards,cards,faced_up_pile, yaniv


def yaniv_game():
    global yaniv
    while yaniv == False:
        for player in range(1,players+1):
            if yaniv == True:
                break
            players_cards,cards,faced_up_pile,yaniv = player_turn(player)

    return players_cards, cards, faced_up_pile, yaniv

players_cards, cards, faced_up_pile, yaniv = yaniv_game()

print(players_cards)

print(cards)

print(faced_up_pile)



