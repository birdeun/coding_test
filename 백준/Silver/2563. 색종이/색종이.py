n = int(input())
A = [[0]*100 for _ in range(100)]

for i in range(n):
    x, y = map(int, input().split())
    
    for j in range(x, x+10):
        for k in range(y, y+10):
            A[j][k] = 1
    
sum = 0
for i in range(0, 100):
    for j in range(0, 100):
        if A[i][j] == 1:
            sum += 1

print(sum)