def minimumBribes(q):
    bribes=0
    for i,o in enumerate(q):
        cur = i+1

        if o-cur > 2:
            print("Too chaotic")

        for k in q[max(o-2,0):i]:
            if k > o:
                bribes += 1
    
    print(bribes)




q = list(map(int,input().rstrip().split()))

minimumBribes(q)