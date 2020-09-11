# cook your dish here
t = int(input())
while t>0:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()[:n]))
    lst = [0]*n
    count = 1
    for i in range(1):
        for j in range(n):
            if arr[j] < arr[i]:
                count += 1
        lst[i] = count
    c = arr[-1]
    count = 1
    for k in range(n):
        if arr[k] > c:
            count += 1
    lst[-1] = count
    
    for i in range(1,n-1):
        count = 1
        for j in range(0,i):
            if arr[j] > arr[i]:
                count += 1
        for k in range(i,n):
            if arr[k] < arr[i]:
                count += 1
        lst[i] = count
    print(str(min(lst)) + " " + str(max(lst)))
            
#1% is correct only
