# from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_cipher(direction, text, shift):

    if direction == 'encode':
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += letter
        print(f"Your encoded message is {cipher_text}")

    elif direction == 'decode':
        decrypted_text = ""
        for letter in text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) - shift
                shifted_position %= len(alphabet)
                decrypted_text += alphabet[shifted_position]
            else:
                decrypted_text += letter
        print(f"Your decoded message is {decrypted_text}")

# print(logo)

chosen_direction = ""
chances_to_try_a_direction = 3
while True and chances_to_try_a_direction > 0:
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if user_input == 'encode':
        chosen_direction = 'encode'
        break
    elif user_input == 'decode':
        chosen_direction = 'decode'
        break
    else:
        print("Wrong input. Please choose 'encode' or 'decode'.")
        chances_to_try_a_direction -= 1

original_text = input("Type your message:\n").lower()
original_text = "".join(original_text.split())

shift_amount = 0
chances_to_try_a_number = 3
while True and chances_to_try_a_number > 0:
    user_input = input("Type the shift number:\n")
    if user_input.isdigit():
        shift_amount = int(user_input)
        break
    else:
        print("Wrong input. Please input only a number.")
        chances_to_try_a_number -= 1

if chances_to_try_a_number > 0 and chances_to_try_a_direction > 0:
    ceaser_cipher(chosen_direction, original_text, shift_amount)






