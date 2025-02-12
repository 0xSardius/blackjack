"""
Classic card game Blackjack! Also known as 21.
Tags: large, game, card game
"""

import random, sys

#constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = "backside"

def main():
    print("""
    Blackjack

    Rules: 
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2-10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.

    On your first play, you can (D)ouble down to increase your bet, but you must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player. The dealer stops hitting at 17.
    """)

    money = 5000

    # main game loop
    while True :
        # check if the player has run out of money
        if money <= 0:
            print("You're broke, Jack!")
            print("Good thing you were only playing with shitcoins!")
            print("Thanks for playing degen!")
            sys.exit()

        # Let the player enter their bet for this round
        print("Money: ", money)
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:

        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # handle player actions:
        print("Bet: ", bet)
        while True: # We keep looping until the player stands or busts
            display_hands(player_hand, dealer_hand, False)
            print()

            # Check if the player has bust:
            if get_hand_value(player_hand) > 21:
                break
        
            # get the player's move, either H, S, or D
            move = get_move(player_hand, money - bet)







if __name__ == "__main__":
    main()
