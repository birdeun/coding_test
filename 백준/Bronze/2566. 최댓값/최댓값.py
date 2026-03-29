A = [(list(map(int, input().split()))) for _ in range(9)]

num = 0
x, y = 0, 0

for i in range(9):
    for k in range(9):
        if A[i][k] > num:
            num = A[i][k]
            x, y = i, k

print(num)
print(x+1,y+1)