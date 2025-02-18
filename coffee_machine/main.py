


from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

items = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

is_on = True
while is_on:
    choice = input(f'What would you like? {items.get_items()} '.lower())
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money.report()
    elif items.find_drink(choice) :
       item = items.find_drink(choice)
       if coffee_maker.is_resource_sufficient(item):
           if money.make_payment(item.cost):
               coffee_maker.make_coffee(item)