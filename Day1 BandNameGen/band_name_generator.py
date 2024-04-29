import time
print("Welcome to the Band Name Generator.")
user_city=input("What's name of the city you grew up in?\n")
pet_name=input("What's your pet's name?\n")
band_name=user_city+ " " + pet_name
print("Generating your band name")

for x in range(1,4):
 print("."*x)
 time.sleep(1)

print("Your band name could be",band_name)
