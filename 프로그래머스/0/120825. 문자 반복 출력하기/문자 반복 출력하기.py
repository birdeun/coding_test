# 첫 번째 답
def solution(my_string, n):
    ans = [n * i for i in my_string]
    return ''.join(ans)

# 두 번째 답 (참고)
def solution(my_string, n):
    return ''.join(n * i for i in my_string)