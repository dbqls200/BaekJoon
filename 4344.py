# 4344번 - 평균은 넘겠지

import sys
input = sys.stdin.readline

c = int(input())


for i in range(c):
    average = 0
    result = 0
    score = list(map(int, input().split()))
    
    for j in range(1, score[0] + 1):
        average += score[j]
        
    average /= score[0]

    for j in range(1, score[0] + 1):
        if score[j] > average:
            result += 1

    result = (result / score[0]) * 100
    print('%.3f%%' %result)

