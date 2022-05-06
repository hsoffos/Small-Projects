"""Game ; Use deductive reasoning to guess the number within alotted attempts, leveraging clues"""

import random

num_digits = 3  # Control length of secret number
max_guesses = 10  # Control max guess attempts


def main():
    print('''Bananas! : A Deductive Logic Game
    
    I am thinking of a {}-digit number with no repeated digits. 
    Try to guess what it is! Here are some clues to remember:
    
    When I Say:         That Means:
        Apple            One digit is correct but in the wrong position
        Orange           One digit is correct and in the right position
        Bananas!         No digit is correct.
        
    For example, if the secret number was 359 and your guess was 954, the 
    clues would be Apple Orange.'''.format(num_digits))

    while True: # Main Game Loop
        # Store the secret number
        secret = getSecret()
        print('I have chosen a number!')
        print(' You have {} guess to figure it out!'.format(max_guesses))

        numguesses = 1
        while numguesses <= max_guesses:
            guess = ''
            # Loop until a valid guess
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}: '.format(numguesses))
                guess = input('> ')

