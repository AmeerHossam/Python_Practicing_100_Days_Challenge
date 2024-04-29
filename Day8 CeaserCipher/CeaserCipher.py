import encoding,decoding

is_True = True
while is_True:
    choice = int(input("Enter 1 for encoding, 2 for decoding or 3 for exit"))   
    if choice == 1:
        text = input("Enter your text: ")
        shift = int(input("Enter the shift number: ").strip())
        print(encoding.encoding(text,shift))
    elif choice == 2:
        text = input("Enter your text: ")
        shift = int(input("Enter the shift number: ").strip())
        print(decoding.decoding(text,shift))
    elif choice == 3:
        is_True = False
    else:
        print("You 've entered wrong choice")
