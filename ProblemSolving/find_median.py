def find_median(arr):

#eq for odd : [(n+1)/2]
#eq for even: [(n/2)+(n/2 + 1)]/2
    length = len(arr)
    sorted_list = sorted(arr)
    if length % 2 == 0:
        median = (sorted_list[(length//2 - 1)+sorted_list[(length//2)]])/2
        print(f"{median}")
    else:
        median = (sorted_list[(length//2)])
        print(f"{median}")

n = int(input().strip())
arr = list(map(int,input().rstrip().split())) 
find_median(arr)