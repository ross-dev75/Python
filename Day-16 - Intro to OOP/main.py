from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to order? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        try:
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                print("that worked I think")
        except AttributeError:
            print("Sorry, invalid choice.")