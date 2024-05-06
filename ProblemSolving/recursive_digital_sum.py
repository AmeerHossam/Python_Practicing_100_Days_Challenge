def superDigit(n,k):
    if len(n) == 1:
        return n
    else:
        return k*sum(list(map(int,str(n))))

first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

# k = int(first_multiple_input[1])

# superDigit(n,k)
# str(new)
