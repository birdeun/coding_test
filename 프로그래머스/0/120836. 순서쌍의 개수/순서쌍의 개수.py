# 첫 번째 답
# 완전 탐색 방식 -> 시간복잡도 O(N) 
# n <= 1,000,000 이기 때문에 100만 번 반복함
def solution(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += 1
    return sum

# 두 번째 답 (참고)
# 최적화 -> 시간복잡도 O(√n)
# 1000번이면 연산 끝남
# 약수는 쌍으로 존재하기 때문에, √n 기준으로 대칭임
def solution(n):
    sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += 2
            if i * i == n:
                sum -= 1
    return sum
