""" A simple text-to-morse code converter"""

# Dictionary containing letters/number and their morse code
MORSE_CODE_TAB = {
    'A': '▄ ▄▄▄', 'B': '▄▄▄ ▄ ▄ ▄', 'C': '▄▄▄ ▄ ▄▄▄ ▄', 'D': '▄▄▄ ▄ ▄', 'E': '▄','F': '▄ ▄ ▄▄▄ ▄', 'G': '▄▄▄ ▄▄▄ ▄',
    'H': '▄ ▄ ▄ ▄', 'I': '▄ ▄', 'J': '▄ ▄▄▄ ▄▄▄ ▄▄▄', 'K': '▄▄▄ ▄ ▄▄▄', 'L': '▄ ▄▄▄ ▄ ▄', 'M': '▄▄▄ ▄▄▄', 'N': '▄▄▄ ▄',
    'O': '▄▄▄ ▄▄▄ ▄▄▄', 'P': '▄ ▄▄▄ ▄▄▄ ▄', 'Q': '▄▄▄ ▄▄▄ ▄ ▄▄▄', 'R': '▄ ▄▄▄ ▄', 'S': '▄ ▄ ▄', 'T': ' ▄▄▄ ',
    'U': '▄ ▄▄▄ ▄▄▄', 'V': '▄ ▄ ▄ ▄▄▄ ', 'W': '▄ ▄▄▄ ▄▄▄', 'X': '▄▄▄ ▄ ▄ ▄▄▄', 'Y': '▄▄▄ ▄ ▄▄▄ ▄▄▄', 'Z': '▄▄▄ ▄▄▄ ▄ ▄',
    '1': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄', '2': '▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄', '3': '▄ ▄ ▄ ▄▄▄ ▄▄▄', '4': '▄ ▄ ▄ ▄ ▄▄▄', '5': '▄ ▄ ▄ ▄ ▄',
    '6': '▄▄▄ ▄ ▄ ▄ ▄', '7': '▄▄▄ ▄▄▄ ▄ ▄ ▄', '8': '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄', '9': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄', '0': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄',
    ' ': '/'
}

# Convert User input to morse code
def convert_com(user_input):
    for char in user_input:
        if char in MORSE_CODE_TAB:
            morse_code = MORSE_CODE_TAB[char] + " "
        else:
            morse_code = "Unknown"
        print(morse_code)

communication = True
while communication:
    # collect user input and converts it to upper case
    text = input("Insert (text/number)s here to convert to Morse code: ").upper()
    if text == 'END':
        communication = False # terminate communication
        print('Communication Terminated')
    else:
        convert_com(text)