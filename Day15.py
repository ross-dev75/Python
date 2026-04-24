MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def pull_ingredients(resource, drank):
    for ingredient, amount in drank["ingredients"].items():
        resource[ingredient] -= amount
    return resource


def check_resources(resource, drank):
    for ingredient, amount in drank["ingredients"].items():
        if resource.get(ingredient, 0) < amount:
            return False
    return True


def process_coins(resource, drank):
    """ Pay for the drink - once payment is successful, we call a function to remove the required ingredients from our resources."""
    drank_cost = drank["cost"]
    print("Please insert coins.")
    try:
        customer_payment = int(input("How many quarters? :")) * 0.25
        customer_payment += int(input("How many dimes? :")) * 0.10
        customer_payment += int(input("How many nickles? :")) * 0.05
        customer_payment += int(input("How many pennies? :")) * 0.01
    except ValueError:
        print("Invalid input. Please enter numbers only. Money refunded.")
        return resource

    if customer_payment >= drank_cost:
        change_required = round(customer_payment - drank_cost, 2)
        resource["money"] += drank_cost
        pull_ingredients(resource, drank)
        if change_required > 0:
            print(f"Here's your drink! Your change is ${change_required}.")
        else:
            print("Here's your drink!")
    else:
        print("Sorry, that's not enough money. Money refunded.")
    return resource


resources["money"] = 0
input_errors = 0

while input_errors < 5:
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == "off":
        break

    elif selection == "report":
        for key, value in resources.items():
            print(key, value)

    elif selection in MENU:
        available = check_resources(resources, MENU[selection])
        if available:
            process_coins(resources, MENU[selection])
        else:
            print("Sorry, that drink is not currently available.")
    else:
        print("Sorry, that's not a valid option.")
        input_errors += 1
