# 첫 번째 답
def solution(strlist):
    rst = []
    for i in strlist:
        rst.append(len(i))
    return rst

# 두 번째 답
# 리스트 컴프리헨션
def solution(strlist):
    ans = [len(i) for i in strlist]
    return ans