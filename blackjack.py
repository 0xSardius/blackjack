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

            # Handle the player actions:
            if move == "D":
                # If the player is doubling down, they can increase their bet:
                additional_bet = getBet(min(bet, (money - bet)))
                bet += additional_bet
                print(f"Bet increased to {bet}.")
                print("Bet: ", bet)
            
            if move in ("H", "D"):
                # Hit/Double: draw a card:
                new_card = deck.pop()
                rank, suit = new_card
                print(f"You drew a {rank} of {suit}.")
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    # player busts
                    continue
            
            if move in ("S", "D"):
                # stand/doubling down stops the player's turn
                break
        
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                # The dealer hits :
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break # The dealer has busted.
                input("Press Enter to continue...")
                print("\n\n")

        # show the final hands:
        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        # handle whether the player won, lost or tied:
        if dealer_value > 21:
            print(f"Dealer busts! You win ${bet}!")
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print(f"You lose! The dealer wins ${bet}!")
            money -= bet
        elif player_value > dealer_value:
            print(f"You win ${bet}!")
            money += bet
        elif player_value == dealer_value:
            print("It's a tie, the bet is returned to you.")
        
        input("Press Enter to continue...")
        print("\n\n")

def get_bet(max_bet):
    """Ask the player how much they want to be for this round."""
    while True: # Keep asking until they enter a valid amount.
        print(f"How much do you want to bet motherfucker? (1-{max_bet}, or QUIT)")
        bet = input('> ').upper().strip()
        if bet == "QUIT":
            print("Thanks for playing asshole!")
            sys.exit()
        
        if not bet.isdecimal():
            continue # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet # player entered a valid bet

def get_deck():
    """ Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """ Show the player's and the dealer's cards. Hide the dealer's first card if show_dealer_hand is False."""
    print()
    if show_dealer_hand:
        print(f"DEALER: {get_hand_value(dealer_hand)}")
        display_cards(dealer_hand)
    else:
        print("DEALER: ????")
        # Hide the dealer's first card:
        display_cards([BACKSIDE] + dealer_hand[1:])
    
    # Show the player's cards:
    print(f"PLAYER: {get_hand_value(player_hand)}")
    display_cards(player_hand)

def get_hand_value(cards):







if __name__ == "__main__":
    main()
