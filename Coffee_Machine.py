import main
resources = main.resources
menu = main.MENU
units = main.units

def ingredients_available(required_ingredients):
    for _ in required_ingredients:
        if required_ingredients[_] > resources[_]:
            print(f"Sorry, there is  not enough {_}")
            return False
    return True

def process_money():
    print("Please insert coins.")
    total  = int(input("How many quarters?:"))*0.25
    total += int(input("How many dimes?:"))*0.10
    total += int(input("How many nickels?:"))*0.05
    total += int(input("How many pennies?:"))*0.01
    return total

def payment_successful(paid_money, required_money):
    if paid_money >= required_money:
        change = round(paid_money - required_money, 2)
        resources["money"] += required_money
        print(f"Here is your ${change} change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_drink(drink_name, ingredients):
    for _ in ingredients:
        resources[_] -= ingredients[_]
    print(f"Here is your {drink_name}☕. Enjoy!")

coffee_machine = True

while coffee_machine:
     drink = input("What would you like? (espresso/latte/cappuccino):").lower()

     if drink == "off":
         print("Goodbye!")
         coffee_machine = False
     elif drink == "report":
         for key,value in resources.items():
             unit = units[key]
             if key == "money":
                 print(f"{key}: {unit}{value}")
             else:
                 print(f"{key}: {value}{unit}")
     else:
         if ingredients_available(menu[drink]["ingredients"]):
             payment = process_money()
             if payment_successful(payment, menu[drink]["cost"]):
                make_drink(drink,menu[drink]["ingredients"])