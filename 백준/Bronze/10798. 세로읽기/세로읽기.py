A = [(list(input())) for _ in range(5)]

for i in range(15):
    for k in range(5):
        if i < len(A[k]):   # (존재) k번째 행에 i번째 열이 존재하는가?
            print(A[k][i], end='')