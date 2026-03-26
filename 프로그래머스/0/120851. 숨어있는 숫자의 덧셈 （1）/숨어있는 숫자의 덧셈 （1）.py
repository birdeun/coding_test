# 첫 번째 답
# 아스키 코드 활용
def solution(my_string):
    sum = 0
    for k in my_string:
        if '0' <= k <= '9':
            sum += int(k)
    return sum

# 두 번째 답
def solution(my_string):
    sum = 0
    num = '1234567890'
    for i in range(len(my_string)):
        if my_string[i] in num:
            sum += int(my_string[i])
    return sum