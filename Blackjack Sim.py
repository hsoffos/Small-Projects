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
    print("""Blackjack : The classic card game
    
    Rules""")