def decoding(text,shift):
    length = len(text)
    decoded_str=""
    for i in range(length):
        if text[i].isupper():
            decoded_str += chr((ord(text[i]) - 65 - shift)%26 +65)
        elif text[i].islower():
            decoded_str += chr((ord(text[i]) -97 - shift)%26 +97)
        else:
            decoded_str += text[i]
    return decoded_str