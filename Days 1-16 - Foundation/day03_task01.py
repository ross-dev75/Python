# Pizza price calculator!

# Example of simple if/else loops, while loops, and nested loops.
# Try to improve it!
# Note: An alternative to declaring price variables would have been to start
# the value of the bill at '0', using a variable, and increment it based on
# the users selections.


# Pizza prices (cash only, no change!)
small_price = 15
medium_price = 20
large_price = 25
small_pep_price = 2
med_or_large_pep_price = 3
extra_cheese_price = 1


print("\n\n\nWelcome to Python Pizza Deliveries!\n\n      Let's eat!")

print("---------MENU---------")
print("Pizzas:\n"
      "Small =  $15   (+2 for pepperoni)\n"
      "Medium = $20   (+3 for pepperoni)\n"
      "Large =  $25   (+3 for pepperoni)")
print("Extra Cheese on Any Pizza = $1\n")


# this while loop capitalizes the input for courtesy, checks that it's valid, and either
# continues with the program or asks the user the same question again.
size = input("What size pizza do you want? Small, Medium or Large: ")
size = size.title()
while size != "Small" and size != "Medium" and size != "Large":
    print("You entered an invalid choice. Please enter either 'Small' or 'Medium' or 'Large'.")
    size = input("What size pizza do you want? Small, Medium or Large: ")
    size = size.title()
print ("Perfect! You would like a " + size + " pizza.")

# While loop capitalizes the input for courtesy, checks that it's valid, and either
# continues with the program or asks the user the same question again.
pepperoni = input("Do you want pepperoni on your pizza? Yes or No: ")
pepperoni = pepperoni.title()
while pepperoni != "Yes" and pepperoni != "No":
    print("You entered an invalid choice. Please enter either 'Yes' or 'No'.")
    pepperoni = input("Do you want pepperoni on your pizza? Yes or No: ")
    pepperoni = pepperoni.title()
if pepperoni == "Yes":
    print ("Perfect! You would like pepperoni on your pizza.")

# While loop capitalizes the input for courtesy, checks that it's valid, and either
# continues with the program or asks the user the same question again.
extra_cheese = input("Do you want extra cheese? Yes or No: ")
extra_cheese = extra_cheese.title()
while extra_cheese != "Yes" and extra_cheese != "No":
    print("You entered an invalid choice. Please enter either 'Yes' or 'No'.")
    extra_cheese = input("Do you want extra cheese? Yes or No: ")
    extra_cheese = extra_cheese.title()
if extra_cheese == "Yes":
    print ("Perfect! You would like extra cheese on your pizza.")


# Now let's calculate the total.


if size == "Small":
    # with pep and extra cheese
    if pepperoni == "Yes" and extra_cheese == "Yes":
        total = small_price + small_pep_price + extra_cheese_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # with pep only
    elif pepperoni == "Yes" and extra_cheese == "No":
        total = small_price + small_pep_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # with extra cheese only
    elif pepperoni == "No" and extra_cheese == "Yes":
        total = small_price + extra_cheese_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # with no pep or extra cheese
    elif pepperoni == "No" and extra_cheese == "No":
        total = small_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # handling errors
    else:
        print("We've experienced an error. Please restart your order. Thank you.")


elif size == "Medium":
    # with pep and extra cheese
    if pepperoni == "Yes" and extra_cheese == "Yes":
        total = medium_price + med_or_large_pep_price + extra_cheese_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # with pep only
    elif pepperoni == "Yes" and extra_cheese == "No":
        total = medium_price + med_or_large_pep_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # with extra cheese only
    elif pepperoni == "No" and extra_cheese == "Yes":
        total = medium_price + extra_cheese_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # with no extras
    elif pepperoni == "No" and extra_cheese == "No":
        total = medium_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # handling errors
    else:
        print("We've experienced an error. Please restart your order. Thank you.")


elif size == "Large":
    # with pep and extra cheese
    if pepperoni == "Yes" and extra_cheese == "Yes":
        total = large_price + med_or_large_pep_price + extra_cheese_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # with pep only
    elif pepperoni == "Yes" and extra_cheese == "No":
        total = large_price + med_or_large_pep_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # with extra cheese only
    elif pepperoni == "No" and extra_cheese == "Yes":
        total = large_price + extra_cheese_price
        print(f"\nYour total price is ${total}.00 dollars.")
    elif pepperoni == "No" and extra_cheese == "No":
        total = large_price + extra_cheese_price
        print(f"\nYour total price is ${total}.00 dollars.")
    # handling errors
    else:
        print("We've experienced an error. Please restart your order. Thank you.")

else:
    #handling errors
    print("We've experienced an error. Please restart your order.")

print("Thank you for your order. I hope it's great!\n\n"
      "----------------------------------\n"
      "See you next time at Python Pizza!\n"
      "----------------------------------")
