import random
def passwordGenerator(letters,numbers,symbols):
    password = ""
    password_length = letters+numbers+symbols
    l=["a", "b", "c", "d", "e","f", "g", "h",
       "i", "j", "k","l", "m", "n", "o", "p",
       "q","r", "s", "t", "u", "v", "w","x",
       "y", "z", "A","B","C","D","E","F","G",
       "H","I","J","K","L","M","N","O","P","Q",
       "R","S","T","U","V","W","X","Y","Z"]
    n=["0","1","2","3","4","5","6","7","8","9"]
    s=["$","#","!","%","&"]
    for _ in range(letters):
        password += random.choice(l)
    for _ in range(numbers):
        password += random.choice(n)
    for _ in range(symbols):
        password += random.choice(s)
    return f"new password easy way: {password} , {len(password)}, {password_length}"

def passwordGenHard(letters,numbers,symbols):
    l=["a", "b", "c", "d", "e","f", "g", "h",
       "i", "j", "k","l", "m", "n", "o", "p",
       "q","r", "s", "t", "u", "v", "w","x",
       "y", "z", "A","B","C","D","E","F","G",
       "H","I","J","K","L","M","N","O","P","Q",
       "R","S","T","U","V","W","X","Y","Z"]
    n=["0","1","2","3","4","5","6","7","8","9"]
    s=["$","#","!","%","&"]
    password = []
    for _ in range(letters):
        password += (random.choice(l))
    for _ in range(numbers):
        password += (random.choice(n))
    for _ in range(symbols):
        password += (random.choice(s))
    random.shuffle(password)
    new_password = ""
    for i in range(len(password)):
        new_password += password[i]
    
        
    return f"new password hard way: {new_password} , {len(new_password)}"
print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your your password?"))
numbers = int(input("How many numbers would you like in your your password?"))
symbols = int(input("How many symbols would you like in your your password?"))
print(passwordGenerator(letters,numbers,symbols))
print(passwordGenHard(letters,numbers,symbols))