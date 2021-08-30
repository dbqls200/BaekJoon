# 2775번 - 부녀회장이 될테야

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    sum = 0
    arr = [[0] * n for i in range(k + 1)]
    arr[0] = list(map(lambda x: x, range(1, n + 1)))

    for i in range(1, k + 1):
        sum = 0
        for j in range(n):
            sum += arr[i - 1][j]
            arr[i][j] = sum

    print(arr[k][n - 1])