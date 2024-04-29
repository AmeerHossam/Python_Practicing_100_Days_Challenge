def PalindromeIndex(s):
    length = len(s)
    def isPalindrome(s): # isPalindrome(aaaad)
        if len(s) <= 1:
            return True
        
        i,j = 0,len(s)-1
        while(i<j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            return True
    i , j = 0,len(s)-1
    while i < j :
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
           if isPalindrome(s[i+1:j+1]): #s="baaaad" 5 indeces 
               return i
           elif isPalindrome(s[i:j]):
               return j
        return -1
    return -1    
    
            
s = input().split()

print(PalindromeIndex(s))