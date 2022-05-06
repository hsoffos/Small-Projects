"""Bitmap Message : Displays a text message according to the provided bitmap image"""

import sys

# Try changing the string to anything else

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Bitmap Message')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap
for line in bitmap.splitlines():
    for i, bit in enumerate(line):  # Loop over each char in the line
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')  # Print a character from the message
    print()  # New line