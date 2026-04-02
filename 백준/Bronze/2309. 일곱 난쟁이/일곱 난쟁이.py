t = [int(input()) for _ in range(9)]

chk = sum(t) - 100

for i in range(9):
    for j in range(i+1, 9):

        if t[i] + t[j] == chk:
            a, b = t[i], t[j]
            break

t.remove(a)
t.remove(b)
t.sort()

for i in range(len(t)):
    print(t[i])