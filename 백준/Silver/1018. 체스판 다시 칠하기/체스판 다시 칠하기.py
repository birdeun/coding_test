# 8x8 크기 체스판 만들기
# 1. 왼위가 흰색인 경우
# 2. 왼위가 검은색인 경우

n,m = map(int, input().split())
board = [input() for _ in range(n)]
rst = 64

# 나의 생각 ....
# 한 줄에 최대한 WB가 균등하게 있거나 차이가 적은 게 유리함
# for문 돌려서 0 ~ n까지 |B-W|가 가장 작은 i 선택하기
# board[0][0] = W or B 체크해서 순서대로 맞추고 바뀐 부분 chk += 1 하기

# 정답
for i in range(n - 7):
    for j in range(m - 7):
        ws = 0      # 왼위 = W
        bs = 0      # 왼위 = B

        for x in range(8):
            for y in range(8):
                cur = board[i + x][j + y]

                if (x + y) % 2 == 0:    # 짝수자리 판별
                    if cur != 'W':      # 1. 짝수자리가 W가 아닐 때
                        ws += 1         #    ws의 경우, B > W 로 바꿔야 함
                    if cur != 'B':      # 2. 짝수자리가 B가 아닐 때
                        bs += 1         #    bs의 경우, W > B 로 바꿔야 함
                
                else:                   # 홀수자리 판별
                    if cur != 'W':      # 1. 홀수자리가 W가 아닐 때
                        bs += 1         #    bs의 경우, B > W 로 바꿔야 함
                    if cur != 'B':      # 2. 홀수자리가 B가 아닐 때
                        ws += 1         #    ws의 경우, W > B 로 바꿔야 함

        rst = min(ws, bs, rst)
print(rst)

# ========================================================================

# for i in range(n - 7):
#     for j in range(m - 7):
#         ws = 0
#         bs = 0

#         for x in range(i, i+8):
#             for y in range(j, j+8):
#                 if (x + y) % 2 == 0:
#                     if board[x][y] != 'W':

#                 # 이렇게 cur 안 쓰고 직접 사용하는 버전도 있음