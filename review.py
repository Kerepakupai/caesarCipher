import os

from logo import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

# TODO-1: Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text: str, shift_amount: int) -> None:
    """Takes a text and return a cipher text"""
    cipher_text = ""
    alphabet_size = len(alphabet)
    # TODO-2: Inside the 'encrypt' funtion , shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    for letter in plain_text:
        position = alphabet.index(letter)
        cipher_position = position + shift_amount
        if cipher_position > alphabet_size - 1:
            cipher_position = cipher_position % alphabet_size

        cipher_letter = alphabet[cipher_position]
        cipher_text += cipher_letter

    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text: str, shift_amount: int) -> None:
    plain_text = ""
    alphabet_size = len(alphabet)
    for letter in cipher_text:
        position = alphabet.index(letter)
        plain_position = position - shift_amount
        if plain_position < 0:
            plain_position = plain_position % alphabet_size

        plain_letter = alphabet[plain_position]
        plain_text += plain_letter

    print(f"The decode text is {plain_text}")


def caesar(text, shift, direction):
    output_text = ""
    alphabet_size = len(alphabet)

    if direction == "decode":
        shift *= -1

    for letter in text:
        if not letter in alphabet:
            output_text += letter
        else:
            position = alphabet.index(letter) + shift

            if position > alphabet_size - 1 or position < 0:
                position %= alphabet_size

            output_text += alphabet[position]

    print(f"The {direction}d text is {output_text}")


# TODO-3: Call the encrypt function and pass in the user inputs.
if __name__ == "__main__":
    should_continue = True

    while should_continue:
        os.system("clear")
        print(logo)

        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
        ).lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift numer:\n"))
        caesar(text, shift, direction)

        answer = input(
            "Type 'yes' if you want to go again. Otherwise type 'no'."
        ).lower()

        if answer != "yes":
            should_continue = False
            print("Goodbye!")
