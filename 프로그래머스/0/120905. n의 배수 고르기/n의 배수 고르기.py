# 첫 번째 답
# 기본형
def solution(n, numlist):
    rst = []
    for i in numlist:
        if i % n == 0:
            rst.append(i)
    return rst

# 두 번째 답 (참고)
# 리스트 컴프리헨션 -> 내부적으로 최적화되어 있어 약간 빠름
def solution(n, numlist):
    ans = [i for i in numlist if i % n == 0]
    return ans
