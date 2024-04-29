def sort_by_letters(arr):
    arr.sort(reverse=True,key=lambda x: len(x))

    print(arr)


arr=list(map(str, input("Enter the letters:\n>>").rstrip().split()))

sort_by_letters(arr)