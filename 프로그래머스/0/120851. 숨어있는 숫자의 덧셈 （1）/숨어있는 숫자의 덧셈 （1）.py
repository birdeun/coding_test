def solution(my_string):
    sum = 0
    for k in my_string:
        if '0' <= k <= '9':
            sum += int(k)
    return sum