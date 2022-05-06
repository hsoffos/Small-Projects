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

    while True:  # Main Game Loop
        # Store the secret number
        secretnum = getSecret()
        print('I have chosen a number!')
        print(' You have {} guess to figure it out!'.format(max_guesses))

        numguesses = 1
        while numguesses <= max_guesses:
            guess = ''
            # Loop until a valid guess
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}: '.format(numguesses))
                guess = input('> ')

            clues = getClues(guess, secretnum)
            print(clues)
            numguesses += 1

            if guess == secretnum:
                break  # Correct answer, break out of guess loop
            if numguesses > max_guesses:
                print('You ran out of guesses! =(')
                print('The answer was {}'.format(secretnum))

        # Ask if player wants to play again
        print('Do you want to play again? ( Y / N )')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')


def getSecret():
    """Returns a string num_digits long of unique random digits"""
    numbers = list('0123456789')  # Create the list of digits 0-9
    random.shuffle(numbers)  # Shuffle the list for random secret

    # Get the first num_digits in the string
    secretnum = ''
    for i in range(num_digits):
        secretnum += str(numbers[i])
    return secretnum

def getClues(guess, secretnum):
    """Reads the guess and outputs string of clues"""
    if guess == secretnum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretnum[i]:
            clues.append('Orange')  # Correct digit, correct place
        elif guess[i] in secretnum:
            clues.append('Apple')  # Correct digit, incorrect place

    if len(clues) == 0:
        return 'Bananas!'
    else:
        # Sort the clues alphabetically so order is not a give-away
        clues.sort()
        return ' '.join(clues)  # Join the list of clues into one string


# If the program is run instead of imported, run the game:
if __name__ == '__main__':
    main()
