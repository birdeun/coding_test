t = int(input())
A = [list(map(int, input().split())) for _ in range(t)]

for i in range(t):
    A[i].sort()
    print(A[i][-3])