t = int(input())
while t>0:
    t -= 1
    n = int(input())
    total = n*(n+1) // 2
    if total%2 == 0 and total>0:
        half = total // 2
        s = 0
        count = 0
        for i in range(n,n//2,-1):
            s += i
            count += 1  
            if s > half:
                print(count)
                break
            elif s == half:
                a = i-1
                rem = n-a
                print(sum(range(1,a)) + sum(range(1,rem+1)))
                break
    else:
        print(0)
