def format_name():
    f_name = input("Enter your First name: ")
    l_name = input("Enter your Last name: ")

    return f"Name is {f_name.capitalize()} {l_name.capitalize()}"

print(format_name())