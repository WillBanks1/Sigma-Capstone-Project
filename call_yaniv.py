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
        print(f'Player {player} called yaniv and won with a score of {
              player_scores[player-1]}')
        print('The final scores are:')
        for i in range(players+1):
            print(f'Player {i+1}: {player_scores[i]}')

    elif player_scores.index(player_scores[player-1]) != winner_index:
        yaniv = True
        print(f'Player {player} called yaniv with a score of {
              player_scores[player-1]}.')
        for i in winner_index:
            if i == player:
                continue
            print(f'But player {i+1} scored {player_scores[i]}')

        print(f'Player {player + 1} loses.')
        print('The final scores are:')
        for i in range(players+1):
            print(f'Player {i+1}: {player_scores[i]}')

    return yaniv
