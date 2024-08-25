import time
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def print_report(self):
        """Print the current resources"""
        for key in self.resources:
            if key == "water" or key == "milk":
                print(f"{key}: {self.resources[key]} ml")
            else:
                print(f"{key}: {self.resources[key]} g")

    def is_resource_sufficient(self,order_ingredients):
        """Check resources"""
        is_enough = True
        for item in order_ingredients:
            if order_ingredients[item] >= self.resources[item]:
                print(f"Sorry there is no enough {item}.")
                is_enough = False
            return is_enough
    def make_coffee(self,drink_name,order_ingredients):
        """Deduct the required ingredients from the resources"""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"your {drink_name} is in progress")
        print("...")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(f"Here is your {drink_name}") 
