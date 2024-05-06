def flippingMatrix(matrix):
    # Write your code here
    length = len(matrix)

    s = 0

    for i in range(length//2): #i = 0,1
        for j in range(length//2): #j = 0,1
            s += max(matrix[i][j],matrix[i][length-j-1],matrix[length-i-1][j],matrix[length-i-1][length-j-1])
            
            # i=0 j=0 >> (107,15,75,112) Max=112
            # i=0 j=1 >> (54,128,15,28)  Max=128
            # i=1 j=0 >> (12,138,100,85) Max=138
            # i=1 j=1 >> (75,110,96,34)  Max=110

    print(s)
#4
n = int(input().strip())

matrix = []

for _ in range(n):
    matrix.append(list(map(int,input().rstrip().split())))
# 107 54 128 15
# 12 75 110 138
# 100 96 34 85
# 75 15 28 112
flippingMatrix(matrix)

