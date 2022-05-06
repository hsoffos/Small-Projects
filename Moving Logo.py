import sys
import random
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up constraints
WIDTH, HEIGHT = bext.size()
# Last column in windows adds newline automatically, so reduce width by 1
WIDTH -= 1

NUMBER_OF_LOGOS = 5  # Try 1-100
PAUSE_AMOUNT = 0.2  # Try 1.0 - 0.0
# Try changing the following list to fewer colors
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dicts:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # Generate some logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # X must be even to hit the corner
            logos[-1][X] -= 1

    cornerbounces = 0  # Count how many times the logo hits a corner
    while True:  # Main loop
        for logo in logos:  # Handle each logo in the logo list
            # Erase logo's current location:
            bext.goto(logo[X], logo[Y])
            #print('   ', end='')  # Try commenting this line out

            original_direction = logo[DIR]

            # See if the logo bounces off the corners
            if logo[X] == 2 and logo[Y] == 1:
                logo[DIR] = DOWN_RIGHT
                cornerbounces += 1
            elif logo[X] == 2 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerbounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 1:
                logo[DIR] = DOWN_LEFT
                cornerbounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerbounces += 1

            # Logo bounces off left edge
            elif logo[X] == 2 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 2 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # Logo bounces off right edge
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # Logo bounces off top edge
            elif logo[Y] == 1 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 1 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # Logo bounces off bottom edge
            elif logo[Y] == HEIGHT - 3 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != original_direction:
                logo[COLOR] = random.choice(COLORS)  # Change color when bounce

            # Move the logo (X moves by 2 because terminal characters are twice as tall as wide)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Display num corner_bounces
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerbounces, end='')

        for logo in logos:
            # Draw the logos at new locations
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()  # Required for bext programs
        time.sleep(PAUSE_AMOUNT)


# If this program was run, not imported, run the game
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo')
        sys.exit()  # When Ctrl-C is pressed, end the program
