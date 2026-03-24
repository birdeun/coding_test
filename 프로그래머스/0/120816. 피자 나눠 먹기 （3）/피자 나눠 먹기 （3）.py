# 첫 번째 답
def solution(slice, n):
    return (n // slice) if (n % slice == 0) else (n // slice + 1)

# 두 번째 답
def solution(slice, n):
    return (n - 1) // slice + 1
