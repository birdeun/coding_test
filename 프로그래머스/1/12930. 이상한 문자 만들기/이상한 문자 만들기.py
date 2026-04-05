def solution(s):
    word = list(s)
    idx = 0
    
    for i in range(len(word)):
        if word[i] == ' ':
            idx = 0
        else:
            if idx % 2 == 0:
                word[i] = word[i].upper()
            else:
                word[i] = word[i].lower()
            idx += 1
    return ''.join(word)
            