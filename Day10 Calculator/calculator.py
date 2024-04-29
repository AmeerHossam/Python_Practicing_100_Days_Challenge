import Ascii as asc
import time
print("welcome to Amir Calculator")
print(asc.Ascii_art)

def calculator(num1, num2, operation):
    def adding_numbers(num1, num2):
        answer = num1 + num2
        return answer

    def subtracting_numbers(num1, num2):
        answer = num1 - num2
        return answer

    def multiply_numbers(num1, num2):
        answer = num1 * num2
        return answer

    def divide_numbers(num1, num2):
        answer = num1 / num2
        return answer

    if operation == '+':
        return adding_numbers(num1, num2)
    elif operation == '-':
        return subtracting_numbers(num1, num2)
    elif operation == '*':
        return multiply_numbers(num1, num2)
    elif operation == '/':
        return divide_numbers(num1, num2)
    else:
        print("You've entered the wrong operation")

def new():
    num1 = float(input("Enter the first number >> "))

    should_continue = True
    while should_continue:
        operation = input("""
        Enter the operation:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        \n>> """)
        num2 = float(input("Enter the next number >> "))
        answer = calculator(num1, num2, operation)
        print(f"{num1} {operation} {num2} = {answer}")

        user_decision = input(f"Type 'y' to continue calculating with {answer} ,'new' to start new calculation or 'n' to exit >> ").lower()
        if user_decision == "y":
            num1 = answer
        elif user_decision == "n":
            should_continue = False
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
        elif user_decision == "new":
            should_continue = False
            new()
        else:
            print("Invalid input, Calculator exits")
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            should_continue = False

new()
