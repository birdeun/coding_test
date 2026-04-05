def solution(strings, n):
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if strings[i][n] > strings[j][n] or \
            (strings[i][n] == strings[j][n] and strings[i] > strings[j]):
                strings[i], strings[j] = strings[j], strings[i]
    return strings