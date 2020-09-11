t = int(input())

while t>0:
    t -= 1
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()[:n]))
        matrix.append(row)
    count = 0
    for i in range(n-1,-1,-1):
        if matrix[0][i] != (i+1):
            for j in range(0,i+1):
                for k in range(j,i+1):
                    temp = matrix[j][k]
                    matrix[j][k] = matrix[k][j]
                    matrix[k][j] = temp
            count += 1
    print(count)
