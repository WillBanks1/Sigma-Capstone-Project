import random
yaniv = False
card_values = {"1": 1, "2": 2, "3": 3, "4": 4,
               "5": 5, "6": 6, "7": 7, "8": 8,
               "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "0": 0
               }


def shuffle_fresh_pack():
    jokers = ["J0", "J0"]
    suits = ["S", "C", "D", "H"]
    values = ["2", "3", "4", "5", "6", "7",
              "8", "9", "10", "J", "Q", "K"]
    unshuffled_cards = [suit+value for suit in suits for value in values]
    shuffled_cards = list(unshuffled_cards)
    random.shuffle(shuffled_cards)
    return shuffled_cards
