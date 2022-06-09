import os
from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''

    if cipher_direction == 'decode':
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            # if new_position >= len(alphabet) or new_position < 0:
            #   new_position = new_position % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'\nHere\'s the {cipher_direction}d result: {end_text}')


def main():
    option = 'yes'
    while option == 'yes':
        os.system('cls')
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift %= len(alphabet)
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        option = input('\nType \'yes\' if you want to go again. Otherwise type \'no\': ').lower()

    print('Goodbye!!')


if __name__ == '__main__':
    main()
