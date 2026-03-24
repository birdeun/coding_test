# 첫 번째 답
# [] 대신 '' 했어도 됨
def solution(my_string, letter):
    rst = []
    for i in my_string:
        if i != letter:
            rst.append(i)
        else:
            continue
    return ''.join(rst)

# 두 번째 답 (참고)
def solution(my_string, letter):
    return my_string.replace(letter, '')
