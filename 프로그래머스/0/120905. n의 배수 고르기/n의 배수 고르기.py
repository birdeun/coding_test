def solution(n, numlist):
    rst = []
    for i in numlist:
        if i % n == 0:
            rst.append(i)
    return rst