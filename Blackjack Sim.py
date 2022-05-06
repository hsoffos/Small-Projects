"""Blackjack : The classic card game (currently without splitting or insurance)"""
import random
import sys

# Constraints
HEARTS = chr(9829)  # Hearts char
DIAMONDS = chr(9830)  # Diamonds
SPADES = chr(9824)  # Spades
CLUBS = chr(9827)  # Clubs

BACKSIDE = 'backside'


def main():
    print('''Blackjack : The classic card game
    
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000
    while True:
        if money <= 0:  # Check if player out of money
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

        # Player enter bet for this round
        print('Money: ', money)
        bet = getBet(money)

        # Deal cards to player and dealer from the deck
        deck = getDeck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Handle player actions
        print('Bet: ', bet)
        while True:  # Loop until Stand or Bust
            displayHands(player_hand, dealer_hand, False)
            print()

            # Check if player Bust
            if getHandValue(player_hand) > 21:
                break

            # Get player move input, H S or D
            move = getMove(player_hand, money - bet)
            if move == 'D':
                # Double Down, can increase the bet
                additional_bet = getBet(min(bet, money - bet))
                bet += additional_bet
                print('Bet increase to {}.'.format(bet))
                print('Bet: ', bet)

            if move in ('H', 'D'):
                # Hit and Double Down takes another card
                new_card = deck.pop()
                print(new_card)
                rank, suit = new_card
                print('You drew a {} of {}.'.format(rank, suit))
                player_hand.append(new_card)

                if getHandValue(player_hand) > 21:
                    continue  # Player Bust

            if move in ('S', 'D'):
                break  # Stand or Double Down stops the player turn

        # Handle dealer actions
        if getHandValue(player_hand) <= 21:
            while getHandValue(dealer_hand) < 17:  # Dealer hits under 17
                print('Dealer Hits...')
                dealer_hand.append(deck.pop())
                displayHands(player_hand, dealer_hand, False)

                if getHandValue(dealer_hand) > 21:
                    break  # Dealer has busted
                input('Press Enter to continue...')
                print('\n\n')

        # Show final hands
        displayHands(player_hand, dealer_hand, True)

        player_value = getHandValue(player_hand)
        dealer_value = getHandValue(dealer_hand)
        # Handle win / loss / tie
        if dealer_value > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print('You won ${}!'.format(bet))
            money += bet
        elif player_value == dealer_value:
            print('It\'s a tie! The best is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')


def getBet(max_bet):
    """Ask the player how much they want to bet for this round"""
    while True:  # Ask until valid entry
        print('How much do you want to bet? (1-{}, or QUIT)'.format(max_bet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue  # If the player didn't enter number, ask again

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet  # Player entered valid bet


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  # Add the face and ace cards
    random.shuffle(deck)
    return deck


def displayHands(play_hand, deal_hand, show_dealer_hand):
    """Show the player's and dealer's cards. Hide the dealer's first
     card if show_dealer_hand is False"""
    print()
    if show_dealer_hand:
        print('DEALER: ', getHandValue(deal_hand))
        displayCards(deal_hand)
    else:
        print('DEALER: ???')
        # Hide dealer's first card
        displayCards([BACKSIDE] + deal_hand[1:])

    # Show the player's cards
    print('PLAYER: ', getHandValue(play_hand))
    displayCards(play_hand)


def getHandValue(cards):
    """Returns the value of the cards. Facecards are worth 10, aces are
    worth 1 or 11 (picks the most suitable value)"""
    value = 0
    number_of_aces = 0

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]  # card is tuple (rank, suit)
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10  # Face cards are worth 10
        else:
            value += int(rank)  # Numbered cards are worth their number

    # Add value for aces
    value += number_of_aces  # Add 1 per ace
    for i in range(number_of_aces):
        # If another 10 can be added without Bust, do so
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    """Display ll the cards in the cards list"""
    rows = ['', '', '', '', '']  # Text for each row

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Top line of the card
        if card == BACKSIDE:
            # Card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '| ##| '
        else:
            # Print the card's front
            rank, suit = card  # Card is a tuple structure
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row
    for row in rows:
        print(row)


def getMove(play_hand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for
    stand, and 'D' for double down"""
    while True:  # Loop until player enters valid move
        # Determine what moves the player can make
        moves = ['(H)it', '(S)tand']

        # Can double down on first move; can tell because they'll have exactly 2 cards
        if len(play_hand) == 2 and money > 0:
            moves.append('(D)ouble Down')

        # Get the player's move
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move  # Player has entered a valid move
        if move == 'D' and '(D)ouble Down' in moves:
            return move  # Player has entered a valid move


# If the program has been run, not imported
if __name__ == '__main__':
    main()
