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
# TODO: 5. when user chooses coffe, check if sufficient resources
def check_if_resources(order_ingredients) :
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'sorry not enough {item}')
            return False
    return True

# TODO: 6: process coins, if sufficient resources ask to pay
def process_coins():
    print('Please input coins')
    total = int(input('please insert quarters: ')) * 0.25
    total += int(input('please input dimes: ')) * 0.1
    total += int(input('Please input nickles: ')) *0.05
    total += int(input('please input pennies: ')) * 0.01
    return total


# TODO: 7. count coins, if user paid more return change, if not enough print 'insufficient funds'
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f'Here is your change: {change}$')
        global profit
        profit += drink_cost
        return True
    else:
        print(f'Insufficient funds, money refunded : {money_received}')
        return False


# TODO: 8. if enough money and resources, make coffe deduct resources
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your drink {drink_name}')


# TODO: 2. keep printing prompting for input while machine on
is_on = True

while is_on:
# TODO: 1. prompt user for what would they like to do, choose coffe type
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
# TODO: 3. turn off the machine when input is OFF
    if choice == 'off':
        is_on = False
# TODO: 4. print report
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml left')
        print(f'Milk: {resources["milk"]}ml left')
        print(f'Coffee: {resources["coffee"]}g left')
        print(f'Money {profit}$')
    else:
        drink = MENU[choice]
        if check_if_resources(drink['ingredients']) :
            payment = process_coins()
            if is_transaction_successful(money_received=payment, drink_cost=drink['cost']):
                make_coffee(drink_name=choice, order_ingredients=drink['ingredients'])

