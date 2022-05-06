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
        print('Money: ',money)
        bet = getBet(money)