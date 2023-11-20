from resources import MENU
from resources import resources

profit = 0
total_coins = 0
Machine_is_ON = True
is_enough = True


def check_resources(ingredients):
    global is_enough
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"There is not enough {item}.")
            is_enough = False
            return is_enough


def coin_machine():
    global total_coins
    global profit
    quarters = float(input("How many quarters? ")) / 4
    dimes = float(input("How many dimes? ")) / 10
    nickels = float(input("How many nickels? ")) / 20
    pennies = float(input("How many pennies? ")) / 100
    total_coins = quarters + dimes + nickels + pennies
    refund = round((total_coins - MENU[choice]["cost"]), 2)
    if refund > 0:
        print(f"Here is your change: ${refund}")
        profit += round((total_coins - refund), 2)
    return profit, total_coins


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        return True
    else:
        print(f"You have not inserted enough money. ${total_coins} returned.")
        return False


while Machine_is_ON:
    choice = input("What would you like?(espresso/latte/cappuccino) ").lower()
    if choice == "off":
        print("Coffee Machine will now turn OFF.")
        Machine_is_ON = False

    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}ml")
        print(f"Profits: ${profit}")

    else:
        drink = MENU[choice]
        drink_cost = MENU[choice]["cost"]
        check_resources(drink["ingredients"])

        if is_enough:
            profit_to_take, _ = coin_machine()
            profit += profit_to_take
            if is_transaction_successful(total_coins, drink_cost):
                for key in resources:
                    if key in drink["ingredients"]:
                        resources[key] -= drink["ingredients"][key]
