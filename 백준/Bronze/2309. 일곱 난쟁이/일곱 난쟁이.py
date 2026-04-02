t = [int(input()) for _ in range(9)]

chk = sum(t) - 100

for i in t:
    for j in t:
        if i == j:
            continue
        elif i + j == chk:
            a, b = i, j
            break

t.remove(a)
t.remove(b)
t.sort()
for i in range(len(t)):
    print(t[i])