import menu
import coffee_maker
import money_machine

menu = menu.Menu()
menuItems = menu.get_items()
items_in_menu = menu.get_items().split("/")
coffee_maker = coffee_maker.CoffeeMaker()
money_machine = money_machine.MoneyMachine()

machine_on = True

while machine_on:
    order = input(f"What would you like? {menuItems}: ")
    if order in items_in_menu:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        machine_on = False
