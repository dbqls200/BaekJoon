# 5622번 - 다이얼

t = input()
n = []
cnt = 0

for i in range(len(t)):
    if t[i] >= 'A' and t[i] <= 'C':
        n.append(2)
    elif t[i] >= 'D' and t[i] <= 'F':
        n.append(3)
    elif t[i] >= 'G' and t[i] <= 'I':
        n.append(4)
    elif t[i] >= 'J' and t[i] <= 'L':
        n.append(5)
    elif t[i] >= 'M' and t[i] <= 'O':
        n.append(6)
    elif t[i] >= 'P' and t[i] <= 'S':
        n.append(7)
    elif t[i] >= 'T' and t[i] <= 'V':
        n.append(8)
    else:
        n.append(9)

for a in n:
    cnt += a + 1

print(cnt)
