import sys

# Defining the Braille alphabet (O = raised dot, . = no dot)
brai_dict = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..', 
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.', 
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO.O.', 'T': '.OOOO.', 
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO', 
    'Z': 'O..OOO', 
    '0': '.OOOO.', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    ' ': '......'
}

# Braille to English Reverse dictionary 
eng_dict = {v: k for k, v in brai_dict.items()}

# Detecting if the input is Braille or English
def detect_lang(input_string):
    if all(c in 'O.' for c in input_string.replace(' ', '')):
        return 'braille'
    else:
        return 'english'

# Converting English to Braille
def eng_to_brai(text):
    braille = []
    for char in text:
        if char.isupper():
            braille.append('.....O')  # Capitalization symbol
            braille.append(brai_dict[char.upper()])
        elif char.isdigit():
            braille.append('.O.O..')  # Number symbol
            braille.append(brai_dict[char])
        else:
            braille.append(brai_dict.get(char.upper(), '......'))  # Map letters, handle spaces
    return ''.join(braille)

# Convert Braille to English
def brai_to_eng(brai_text):
    result = []
    i = 0
    capitalize_next = False
    is_number = False

    while i < len(brai_text):
        if brai_text[i:i+6] == '.....O':  # Capitalization symbol
            capitalize_next = True
            i += 6
        elif brai_text[i:i+6] == '.O.O..':  # Number symbol
            is_number = True
            i += 6
        else:
            brai_char = brai_text[i:i+6]
            if is_number:
                result.append(eng_dict.get(brai_char, ' '))
                is_number = False
            else:
                letter = eng_dict.get(brai_char, ' ')
                if capitalize_next:
                    result.append(letter.upper())
                    capitalize_next = False
                else:
                    result.append(letter.lower())
            i += 6
    return ''.join(result)

# Main function
def main():
    
    print("Please provide a string to translate.")
    input_string = input()
    language = detect_lang(input_string)

    if language == 'english':
        print(eng_to_brai(input_string))
    else:
        print(brai_to_eng(input_string))

if __name__ == '__main__':
    main()
