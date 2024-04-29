def findZigZagSeq(a,n):
    
    a.sort()
    
    mid = int((n-1)/2)
    
    a[mid],a[n-1]=a[n-1],a[mid]

    st = mid + 1
    ed = n - 2

    while(st<=ed):
        a[st],a[ed]=a[ed],a[st]
        st+=1
        ed-=1
    
    print(a)

n = int(input())
a = list(map(int,input().rstrip().split()))

findZigZagSeq(a,n)