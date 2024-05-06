s = "middle-Outz"
l=len(s)
m = int(input().strip())
new_s=""
for i in range(l):
    if s[i].isupper():
        new_s += chr((ord(s[i])-65+m)%26+65)
    elif s[i].islower():
        new_s += chr((ord(s[i])-97+m)%26+97)
    else:
        new_s += s[i]
    
        

print(new_s)
