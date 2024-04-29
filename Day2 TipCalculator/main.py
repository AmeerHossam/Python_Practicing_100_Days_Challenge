#Calculate the length of strings
print(len("Hello"))

#Data Types:
#Strings
print("Hello"[-1])
#Concatenation
print("123"+"456")

#Boolean
print(True)
#Or
print(False)

num_char = str(len(input("What is your name?")))
# new_num_char=str(num_char)
print("Your name has "+num_char+" characters")

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print(int(two_digit_number[0])+int(two_digit_number[1]))

# 1st input: enter height in meters e.g: 1.65
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
BMI= weight/height*height
print(f"Your BMI is {BMI}")

