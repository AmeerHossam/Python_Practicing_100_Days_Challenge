def encoding(text,shift):
    length = len(text)
    encoded_str=""
    for i in range(length):
        if text[i].isupper():
            encoded_str += chr((ord(text[i]) - 65 + shift)%26 + 65)
        elif text[i].islower():
            encoded_str += chr((ord(text[i]) -97 + shift)%26 +97)
        else:
            encoded_str += text[i]
    return encoded_str