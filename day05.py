import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



# Auto generates password for the user using nine characters, nine numbers, and nine symbols.
# then shuffles the password so that the order (num, char, symb, num, char, symb...) isn't consistent.

print("Welcome to Password Generator Project! Would you like a new password?")
input ("Press Enter to continue...")

random_auto_password = []
x = 0
while x < 9:
    random_auto_password.append(random.choice(letters))
    random_auto_password.append(random.choice(numbers))
    random_auto_password.append(random.choice(symbols))
    x += 1

random.shuffle(random_auto_password)
auto_password = ""
for char in random_auto_password:
    auto_password += char

print(auto_password)

# # User input mode: User states how many letters, numbers, and symbols they want.

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


# # Easy Mode: Generates letters, numbers, and symbols in that order.

# new_password = ""
# for char in range(0, nr_letters):
#     new_password += random.choice(letters)
#
# for symb in range(0, nr_symbols):
#     new_password += random.choice(symbols)
#
# for num in range(0, nr_numbers):
#     new_password += random.choice(numbers)
#
# print(new_password)


# # Hard Mode: Scrambles letters, numbers, and symbols.
#
# new_password_list = []
# for char in range(0, nr_letters):
#     new_password_list += random.choice(letters)
#
# for symb in range(0, nr_symbols):
#     new_password_list += random.choice(symbols)
#
# for num in range(0, nr_numbers):
#     new_password_list += random.choice(numbers)
#
# random.shuffle(new_password_list)
# true_random_password = ""
# for char in new_password_list:
#     true_random_password += char
#
# print(true_random_password)


