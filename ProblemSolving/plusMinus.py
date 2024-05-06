def plusMinus(arr):
    length = len(arr)
    pos_value = 0
    neg_value = 0
    zeros = 0
    for i in arr:
        if i > 0:
            pos_value += 1
        elif i < 0:
            neg_value += 1
        else:
            zeros += 1
    print(f"{pos_value/length:.6f}")
    print(f"{neg_value/length:.6f}")
    print(f"{zeros/length:.6f}")

n = int(input().strip())
arr = list(map(int,input().rstrip().split()))

plusMinus(arr)