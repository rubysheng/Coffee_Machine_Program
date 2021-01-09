from art import logo

print(logo)


# TODO: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def reporting(money, resource):
    """Generate a report that shows the current resource values

    :param float money: total money having been earned
    :param dict resource: the remaining resource in coffee machine
    :return:
    """
    earned = "{:.2f}".format(money)
    print(f"Water: {resource['water']}ml\nMilk: {resource['milk']}ml\nCoffee: {resource['coffee']}g\nMoney: ${earned}")


# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def check_sufficient(coffee, remain):
    """Check resources sufficient

    :param str coffee: type of coffee chosen
    :param dict remain: remained resources
    :return: if all resources are sufficient for making the needed coffee (T or F)
    """
    needed = MENU[coffee]['ingredients']
    for ingredient in needed.keys():
        if remain[ingredient] < needed[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


# TODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def check_payment(coffee):
    """Calculate charge of money (may less than 0)

    :param str coffee: type of coffee chosen
    :return: charge
    """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))  # 25 cents
    dimes = int(input("how many dimes?: "))  # 10 cents
    nickles = int(input("how many nickles?: "))  # 5 cents
    pennies = int(input("how many pennies?: "))  # 1 cents
    total = float(0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies)
    value = MENU[coffee]['cost']
    change = total - value
    change = round(change,2)
    return change


# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
def make_coffee(coffee, unprocessed_resource):
    """Calculate resources left after making the needed coffee

    :param str coffee: type of coffee chosen
    :param dict unprocessed_resource: resources before making the coffee
    :return: resources left after making the coffee
    """
    used = MENU[coffee]['ingredients']
    remained = unprocessed_resource
    for ingredient in used.keys():
        remained[ingredient] = unprocessed_resource[ingredient] - used[ingredient]
    return remained


# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
def check_input(money, resource):
    """Check the user’s input to decide what to do next

    :param float money: total money having been earned
    :param dict resource: the remaining resource in coffee machine
    :return:
    """
    desire = input("What would you like? (espresso/latte/cappuccino): ")
    if desire in ["espresso", "latte", "cappuccino"]:
        coffee_type = desire
        # check if the remaining resource is enough to make this coffee
        # if enough, continue; otherwise, print error.
        if check_sufficient(coffee_type, resource):
            # TODO: 6. Check transaction successful?
            # a. Check that the user has inserted enough money to purchase the drink they selected.
            # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
            # program should say “ Sorry that's not enough money. Money refunded. ”.
            # b. But if the user has inserted enough money, then the cost of the drink gets added to the
            # machine as the profit and this will be reflected the next time “report” is triggered. E.g.
            # Water: 100ml
            # Milk: 50ml
            # Coffee: 76g
            # Money: $2.5
            # c. If the user has inserted too much money, the machine should offer change.
            # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
            # places.
            change = check_payment(coffee_type)
            if change >= 0:
                change = "{:.2f}".format(change)
                print(f"Here is ${change} in change.")
                coffee_type_emoji = "☕️"
                print(f"Here is your {coffee_type} {coffee_type_emoji}️. Enjoy!")
                resource = make_coffee(coffee_type, resource)
                money += MENU[coffee_type]['cost']
            else:
                print(" Sorry that's not enough money. Money refunded. ")

    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine. Your code should end execution when this happens.
    elif desire == "off":
        print("Bye")
        return 0

    elif desire == "report":
        reporting(money, resource)

    check_input(money, resource)


from data import resources
from data import MENU

resource_remain = resources
earned = float(0)
check_input(earned, resource_remain)
