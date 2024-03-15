def player_greeting(player,card_count):
    print(f'Hi player {player}')
    print(f'Your hand is: {players_cards[player-1]}')
    print(f'The previous player played {card_count} card(s)')
    if (card_count == 1) or (card_count == 0):
        print(f'Top card of faced up pile is: {faced_up_pile[0]}')
    else:
        print(f'The top {card_count} cards of the faced up pile are: {faced_up_pile[:card_count]}')
    
    return 
