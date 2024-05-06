from ascii import logo
from menu import MENU , resources
import time
profit = 0
print(logo)
print("Good Morning sir/ma'am")

#Function for printing the report

def print_report():
    """Print the current resources"""
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key}: {resources[key]} ml")
        else:
            print(f"{key}: {resources[key]} g")

def is_resource_sufficient(order_ingredients):
    """Check resources"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}.")
            is_enough = False
        return is_enough

def process_coins():
    """Return total calaculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    """Return True iof the payment accepted"""
    if money_received == drink_cost:
        global profit
        profit += drink_cost
        return True               
    elif payment > drink_cost:
        change = money_received - drink_cost
        if profit < change:
            print(f"Please insert the specific money for your {order}")
            return False
        else:
            profit += drink_cost
            print(f"Here is your change, {change}")
            return True
    else:
        print(f"You didn't insert enough money for {order}, you need to put {drink["cost"]}")
        return False
    
def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"your {drink_name} is in progress")
    print("...")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(f"Here is your {drink_name}") 

is_on = True

while is_on:
    order = input("What would you like? (Espresso/latte/Cappuccino):").lower()

    #Turn off the machine
    if order == "off":
        is_on = False
        print("Bye Bye")

    #print report
    elif order == "report":
        print_report()
        print(f"Money: {profit} $")

    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):    
                make_coffee(order,drink["ingredients"])