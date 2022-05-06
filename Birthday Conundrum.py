"""Birthday Conundrum : Monte Carlo Simulation exploring the famous Birthday Problem"""

import datetime, random


def getBirthdays(numberOfBirthdays):
    """Returns a list of *number* random date objects for birthdays"""
    birthdays = []

    for i in range(numberOfBirthdays):
        # Year is unimportant, so only grab month and day
        startOfYear = datetime.date(2001, 1, 1)

        # Random day in the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once"""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays unique

    # Compare each birthday to all others
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return first matching birthday


# Display calculator intro:
print('''Birthday Conundrum!

The Birthday Problem tells us that in a group of N people, the odds 
that two of them have matching birthdays is surprisingly large. 
This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.

(It's not actually a problem, it's just a surprising result.)''')

# Set up a tuple of months in name order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Ask user until valid entry
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # User has entered a valid amount

print()

# Generate and display the birthdays:
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i!=0:
        # Display a comma for each birthday after first
        print(', ', end='')
    monthName = MONTHS[birthday.month-1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# Determine if there are two birtdays that match
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month -1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays')
print()


# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

# print('Let\'s run another 100,000 simulations.')
simMatch = 0  # How many simulations had matching birthdays in them
for i in range(100_000):
    # Report progress every 10,000
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(simMatch /100_000 * 100, 2)
print('Out of 100,000 simulation of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
