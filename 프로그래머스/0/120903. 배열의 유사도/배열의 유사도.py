def solution(s1, s2):
    sum = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            sum += 1
    return sum
