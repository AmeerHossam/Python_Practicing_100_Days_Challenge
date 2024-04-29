def palindromeIndex(s):
    length = len(s)
    i,j=0,length-1

    def isPalindrome(s):
        if len(s) <= 1:
            return True
        i , j = 0 , len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True
    
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            
        else:
            
            if isPalindrome(s[i+1:j+1]):
                return i
            
            elif isPalindrome(s[i:j]):
                return j
            
    return -1

        
s = input().strip()

print(palindromeIndex(s))

