# 첫 번째 답
def solution(n):
    if (n ** 0.5) % int(n ** 0.5) == 0:
        return 1
    else:
        return 2
    
# 두 번째 답 (간략히)
def solution(n):
    return 1 if (n ** 0.5) % int(n ** 0.5) == 0 else 2