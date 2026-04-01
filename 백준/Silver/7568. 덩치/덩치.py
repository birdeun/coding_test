n = int(input())
spec = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    rank = 1                # 변수 이름 (기본 시작 1)

    for j in range(n):
        if i == j:          # 같은 행끼리는 비교할 필요가 없음
            continue

        if spec[j][0] > spec[i][0] and spec[j][1] > spec[i][1]:
            rank += 1

    print(rank, end=' ')