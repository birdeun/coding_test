# 빙고가 되는 경우
# 1. bingo[i][0] > 세로줄
# 2. bingo[0][j] > 가로줄
# 3. bingo[i][i] and bingo[i][4-i] > 대각선

bingo = [list(map(int, input().split())) for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]
chk = 0

for i in range(5):
    for j in range(5):
        for x in range(5):
            for y in range(5):
                if bingo[x][y] == num[i][j]:
                    bingo[x][y] = 0
                    chk += 1

        boom = 0

        for k in range(5):
            if all(bingo[k][l] == 0 for l in range(5)):
                boom += 1
            if all(bingo[l][k] == 0 for l in range(5)):
                boom += 1

        if all(bingo[a][a] == 0 for a in range(5)):
            boom += 1
        if all(bingo[a][4-a] == 0 for a in range(5)):
            boom += 1
       
        if boom >= 3:
            print(chk)
            exit()