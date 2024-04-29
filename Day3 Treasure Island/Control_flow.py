# print("Welcome to the rollercoaster!")

# height= int(input("What is your height in CM? "))
# if height > 120:
#     print("You can ride the rollercoaster")

# else:
#     print("Sorry, you must be more than 120 cm")


#Leap Year check

year=int(input("Enter the year:"))
if year%4==0:
    if year%100==0:
        if year %400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")
