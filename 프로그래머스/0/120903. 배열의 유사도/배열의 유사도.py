# 첫 번째 답
# 인덱스 접근 필요하다는 단점이 있음
def solution(s1, s2):
    sum = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            sum += 1
    return sum

# 두 번째 답
def solution(s1, s2):
    sum = 0
    for i in s1:
        if i in s2:
            sum += 1
    return sum

# 세 번째 답 (참고)
# set 사용해서 유니크 개수 구하는 방식으로 나타낼 수 있음
def solution(s1, s2):
    return (len(set(s1)&set(s2)))
