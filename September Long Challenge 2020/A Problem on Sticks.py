t = int(input())
for i in range(t):
    a = int(input())
    b = list(map(int, input().split()[:a]))
    if 0 in b:
        print(len(set(b)) - 1)
    else:
        print(len(set(b)))
